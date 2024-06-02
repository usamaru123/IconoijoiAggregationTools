from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView,View
from .models import MenberModel,EventModel,VenueModel,HallTypeModel,HallInfoModel
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect
from matplotlib import pyplot as plt
from . import graph 
import csv,urllib
import datetime
from django.db.models import Q



class Toppage(ListView): #トップページ
    template_name = 'index.html'
    model = EventModel

    def get_context_data(self,*args,**kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = VenueModel.objects.order_by('venuedate').all()
        return ctx
    
class Adminpage(ListView): #トップページ
    template_name = 'admin.html'
    model = EventModel

    def get_context_data(self,*args,**kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = VenueModel.objects.order_by('venuedate').all()
        return ctx


class AnswerList(ListView): #回答一覧ページ
    template_name = 'result.html'
    model = EventModel

    def get_context_data(self,*args,**kwargs,):
        ctx = super().get_context_data(**kwargs)
        qsmodel = MenberModel.objects.filter(venueid=self.kwargs['num']).all()
        venuemodel = VenueModel.objects.get(venueid=self.kwargs['num'])
        performtimes = venuemodel.perform_time.order_by('disp_priority')
        ticketsvalobj = venuemodel.tickettype.order_by('priority')
        floorvalobj = venuemodel.hallset.order_by('priority')
        sheetvalobj = venuemodel.sheettype.order_by('priority')

        ticketsval = [ticket.tickettype for ticket in ticketsvalobj]
        floorsval = [floor.blockname for floor in floorvalobj]
        sheetsval = [sheet.sheet for sheet in sheetvalobj]

        rowmax = venuemodel.rowmax
        columnmax = venuemodel.columnmax

        time = 'matinee'
        

        if(time):
            time = self.request.GET.get('time')

        count = qsmodel.count()

           
        if time == 'evening':
            qs = qsmodel.exclude(ticket2__exact="")
            qsarena = qs.exclude(block_c2__exact="")
            qsrow = qs.exclude(row2__exact="")
            qsfloor = qs.exclude(floor2__exact="")

            ticket = [ticket.ticket2 for ticket in qs]
            block = [block.block_r2 for block in qsarena]
            row = [row.row2 for row in qsrow]
            column = [column.block_c2 for column in qsarena]
            arenasheet = [sheet.sheet2 for sheet in qsarena]

            floor = [floor.floor2 for floor in qsfloor]
            sheet = [sheet.sheet2 for sheet in qs ]
            number = [number.number2 for number in qsfloor]


        else:
            qs = qsmodel.exclude(ticket1__exact="")
            qsarena = qs.exclude(block_c1__exact="")
            qsrow = qs.exclude(row1__exact="")
            qsfloor = qs.exclude(floor1__exact="")

            ticket = [ticket.ticket1 for ticket in qs]
            block = [block.block_r1 for block in qsarena]
            row = [row.row1 for row in qsrow]
            column = [column.block_c1 for column in qsarena]
            arenasheet = [sheet.sheet1 for sheet in qsarena]

            floor = [floor.floor1 for floor in qsfloor]

            sheet = [sheet.sheet1 for sheet in qs ]
            number = [number.number1 for number in qsfloor]

        qs_f_sheet = {}
        histgrams = {}
        item = {}

        for i in range(len(floorsval)):
            qs_f = qsrow.filter(floor1=floorsval[i])
            for j in range(len(sheetsval)):
                qs_f_sheet = qs_f.filter(sheet1=sheetsval[j])
                item[sheetsval[j]] = [int(row.row1 or 0) for row in qs_f_sheet]
                histgrams[floorsval[i]] = graph.Floor_Histogram(item)
        
        ctx['floorhistgrams'] = histgrams

        ticketchart = graph.piecreate(ticket,ticketsval,'チケット種別')
        sheetchart = graph.piecreate(sheet,sheetsval,'座席種別')
        floorchart = graph.piecreate(floor,floorsval,'階層種別')
       # heatmap = graph.Arena_HeatMap(block,column,arenasheet,rowmax,columnmax)
        heatmap2 = graph.Floor_HeatMap(row,number,arenasheet,rowmax,columnmax)
        
        performcount = performtimes.count()
        ctx['ticketchart'] = ticketchart
        ctx['sheetchart'] = sheetchart
        ctx['floorchart'] = floorchart

        ctx['heatmap'] = heatmap2
       # ctx['sheetratio1'] = sheetratio1
        ctx['results'] = qs
        ctx['title'] = venuemodel
        ctx['count'] = count
        ctx['num'] = self.kwargs['num']
        ctx['performcount'] = performcount
        ctx['floorsval'] = floorsval
        return  ctx

class AnswerCreate(CreateView): #回答作成フォーム
    template_name = 'create2.html'
    model = MenberModel
    
    fields = ('venueid','matinee','evening','ticket1','sheet1','floor1','row1','block_r1','block_c1','number1','ticket2','sheet2','floor2','row2','block_r2','block_c2','number2',)
    def get_context_data(self,*args,**kwargs,):
        ctx = super().get_context_data(**kwargs)
        answerObj =  MenberModel.objects.filter(venueid=self.kwargs['num']).all()
        venueObj = VenueModel.objects.get(venueid=self.kwargs['num'])
        performtimes = venueObj.perform_time.order_by('disp_priority')
        blocks = venueObj.hallinfo.halltype.order_by('priority')
        tickets = venueObj.tickettype.order_by('priority')


        c_answer = answerObj.count()
        

        ctx['count'] = c_answer
        ctx['title'] = venueObj
        ctx['results'] = answerObj
        ctx['blocks'] = blocks
        ctx['performtimes'] = performtimes
        ctx['tickets'] = tickets
        return  ctx

    def get_success_url(self):
        
        return reverse_lazy('jsapp:thanks',kwargs={"num":self.kwargs['num']})

class EventCreate(CreateView):
    def get_context_data(self,*args,**kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['events'] = EventModel.objects.all()
        return ctx
    
    template_name = 'event.html'
    model = EventModel
    fields =('eventid','group','eventtype','eventtitle')
    success_url = ('eventcreate')
   
class EventList(ListView):
    template_name = 'eventlist.html'
    model = EventModel
    
class VenueCreate(CreateView):
    def get_context_data(self,*args,**kwargs,):
        ctx = super().get_context_data(**kwargs)
        ctx['events'] = EventModel.objects.all()
        ctx['venues'] = VenueModel.objects.all()
        return  ctx 
    
    template_name= 'venue.html'
    model = VenueModel
    
    fields = ('__all__')
    success_url = ('venuecreate')

class VenueList(ListView):
    model = EventModel
    template_name = 'venuelist.html'
    def get_context_data(self,*args,**kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['venue'] = VenueModel.objects.order_by('venuedate')
        return ctx

class HallinfoCreate(CreateView):
    def get_context_data(self,*args,**kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['hallinfo'] = HallInfoModel.objects.all()
        return ctx

    template_name = 'hallinfo.html'
    model = HallInfoModel

    fields = ('__all__')
    success_url =('hallinfocreate')


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
