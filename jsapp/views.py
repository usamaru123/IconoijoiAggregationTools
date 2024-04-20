from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView,View
from .models import MenberModel,EventModel,VenueModel,HallTypeModel
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect
from matplotlib import pyplot as plt
from . import graph
import tasks
import csv,urllib
import datetime


class Toppage(ListView):
    template_name = 'index.html'
    model = EventModel

    def get_context_data(self,*args,**kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = VenueModel.objects.order_by('venuedate').all()
        return ctx

class AnswerList(ListView):
    template_name = 'result.html'
    model = EventModel



    def get_context_data(self,*args,**kwargs,):
        ctx = super().get_context_data(**kwargs)
        qsmodel = MenberModel.objects.filter(venueid=self.kwargs['num']).all()
        venuemodel = VenueModel.objects.get(venueid=self.kwargs['num'])
        
        qs1 = qsmodel.exclude(ticket1__exact="")
        qs2 = qsmodel.exclude(ticket2__exact="")

        qs1arena  = qs1.exclude(block_c1__exact="")
        qs2arena  = qs2.exclude(block_c2__exact="")

        qs1floor = qs1.exclude(floor1__exact="")
        qs2floor = qs2.exclude(floor2__exact="")

        rowmax = venuemodel.rowmax
        columnmax = venuemodel.columnmax

        time = 'matinee'
        

        if(time):
            time = self.request.GET.get('time')

        count = qsmodel.count()

           
        if time == 'evening':
            qs = qs2
            qsarena = qs2arena
            qsfloor = qs2floor

            block = [block.block_r2 for block in qsarena]
            column = [column.block_c2 for column in qsarena]
            arenasheet = [sheet.sheet2 for sheet in qsarena]

            floor = [floor.floor2 for floor in qsfloor]
            sheet = [sheet.sheet2 for sheet in qs ]
            number = [number.number2 for number in qsfloor]


        else:
            qs = qs1
            qsarena = qs1arena
            qsfloor = qs1floor

            block = [block.block_r1 for block in qsarena]
            column = [column.block_c1 for column in qsarena]
            arenasheet = [sheet.sheet1 for sheet in qsarena]

            floor = [floor.floor1 for floor in qsfloor]
            sheet = [sheet.sheet1 for sheet in qs ]
            number = [number.number1 for number in qsfloor]

        chart = graph.sheetratio(sheet)
        heatmap = graph.Arena_HeatMap(block,column,arenasheet,rowmax,columnmax)
        floorheatmap = graph.Floor_HeatMap(floor,number)

        ctx['chart'] = chart
        ctx['heatmap'] = heatmap
       # ctx['sheetratio1'] = sheetratio1
        ctx['results'] = qs
        ctx['title'] = venuemodel
        ctx['count'] = count
        ctx['num'] = self.kwargs['num']
        return  ctx

class AnswerCreate(CreateView):
    template_name = 'create2.html'
    model = MenberModel
    
    fields = ('venueid','matinee','evening','ticket1','sheet1','floor1','row1','block_r1','block_c1','number1','ticket2','sheet2','floor2','row2','block_r2','block_c2','number2',)
    def get_context_data(self,*args,**kwargs,):
        ctx = super().get_context_data(**kwargs)
        answerObj =  MenberModel.objects.filter(venueid=self.kwargs['num']).all()
        venueObj = VenueModel.objects.get(venueid=self.kwargs['num'])
        performtimes = venueObj.perform_time.order_by('disp_priority')
        blocks = venueObj.hallinfo.halltype.order_by('priority')

        c_answer = answerObj.count()
        

        ctx['count'] = c_answer
        ctx['title'] = venueObj
        ctx['results'] = answerObj
        ctx['blocks'] = blocks
        ctx['performtimes'] = performtimes
        return  ctx

    def get_success_url(self,form):
        item = form.save(commit=False)
        item.save()
        tasks.send_notification(item,'登録')
        return reverse_lazy('jsapp:thanks',kwargs={"num":self.kwargs['num']})


class EventCreate(CreateView):
    template_name = 'event.html'
    model = EventModel
    fields =('eventid','group','eventtype','eventtitle')
    success_url = ('jsapp:eventlist')
   
class EventList(ListView):
    template_name = 'eventlist.html'
    model = EventModel
    
class VenueCreate(CreateView):
    def get_context_data(self,*args,**kwargs,):
        ctx = super().get_context_data(**kwargs)
        ctx['event'] = EventModel.objects.all()
        return  ctx 
    
    template_name= 'venue.html'
    model = VenueModel
    
    fields = ('__all__')
    success_url = ('jsapp:venuelist')

class VenueList(ListView):
    model = EventModel
    template_name = 'venuelist.html'
    def get_context_data(self,*args,**kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['venue'] = VenueModel.objects.order_by('venuedate')
        return ctx


class ThanksView(ListView):
    template_name = 'thanks.html'
    model = EventModel
    def get_context_data(self,*args,**kwargs,):
        ctx = super().get_context_data(**kwargs)
        ctx['results'] = MenberModel.objects.filter(venueid=self.kwargs['num']).all()
        ctx['title'] = VenueModel.objects.get(venueid=self.kwargs['num'])
        return  ctx
    
def csv_export(request,num):
    No = 1
    response = HttpResponse(content_type='text\csv; charset=Shift-JIS')
    now = datetime.datetime.now()
    downloadtime = now.strftime('%Y%m%d_%H%M%S')
    f = str(num) + '集計結果：' + downloadtime +  '.csv'
    header = [
        'No.',
        '日時',
        '昼チケット',
        '昼座席',
        '昼フロア',
        '昼縦ブロック',
        '昼横ブロック',
        '昼列',
        '昼番号',
        '夜チケット',
        '夜座席',
        '夜フロア',
        '夜縦ブロック',
        '夜横ブロック',
        '夜列',
        '夜番号'
        ]
    filename = urllib.parse.quote((f).encode('utf-8'))
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
    write = csv.writer(response)
    write.writerow(header)
    for result in MenberModel.objects.filter(venueid=num).order_by('timedate'):
        write.writerow([
            No,
            result.timedate,
            result.ticket1,
            result.sheet1,
            result.floor1,
            result.block_r1,
            result.block_c1,
            result.row1,
            result.number1,
            result.ticket2,
            result.sheet2,
            result.floor2,
            result.block_r2,
            result.block_c2,
            result.row2,
            result.number2,
            ])
        No = No + 1
    return response
