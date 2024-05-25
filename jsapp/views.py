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
        floorvalobj = venuemodel.hallinfo.halltype.order_by('priority')

        ticketsval = [ticket.tickettype for ticket in ticketsvalobj]
        floorsval = [floor.blockname for floor in floorvalobj]

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

            qs_f1 = qs.filter(Q(floor1='1階席')|Q(floor1='１階席')|Q(floor1='アリーナ席')|Q(floor1='アリーナ席'))

            ticket = [ticket.ticket1 for ticket in qs]
            block = [block.block_r1 for block in qsarena]
            row = [row.row1 for row in qsrow]
            column = [column.block_c1 for column in qsarena]
            arenasheet = [sheet.sheet1 for sheet in qsarena]

            floor = [floor.floor1 for floor in qsfloor]

            sheet = [sheet.sheet1 for sheet in qs ]
            number = [number.number1 for number in qsfloor]

        qs_f1 = qs.filter(Q(floor1='1階席')|Q(floor1='１階席')|Q(floor1='アリーナ席')|Q(floor1='アリーナ席'))
        qs_f2 = qs.filter(Q(floor1='2階席')|Q(floor1='２階席'))
        qs_f3 = qs.filter(Q(floor1='3階席')|Q(floor1='３階席'))
        qs_f4 = qs.filter(Q(floor1='4階席')|Q(floor1='４階席'))

        f1_ippan = qs_f1.filter(sheet1='一般席')
        f1_cameko = qs_f1.filter(sheet1='カメコエリア席')
        f1_josei = qs_f1.filter(sheet1='女性エリア席')
        f1_chaku = qs_f1.filter(sheet1='着席指定席')

        f2_ippan = qs_f2.filter(sheet1='一般席')
        f2_cameko = qs_f2.filter(sheet1='カメコエリア席')
        f2_josei = qs_f2.filter(sheet1='女性エリア席')
        f2_chaku = qs_f2.filter(sheet1='着席指定席')

        f3_ippan = qs_f3.filter(sheet1='一般席')
        f3_cameko = qs_f3.filter(sheet1='カメコエリア席')
        f3_josei = qs_f3.filter(sheet1='女性エリア席')
        f3_chaku = qs_f3.filter(sheet1='着席指定席')

        f4_ippan = qs_f4.filter(sheet1='一般席')
        f4_cameko = qs_f4.filter(sheet1='カメコエリア席')
        f4_josei = qs_f4.filter(sheet1='女性エリア席')
        f4_chaku = qs_f4.filter(sheet1='着席指定席')

        f1_row_ippan = [f1_row.row1 for f1_row in f1_ippan]
        f1_row_cameko = [f1_row.row1 for f1_row in f1_cameko]
        f1_row_josei = [f1_row.row1 for f1_row in f1_josei]
        f1_row_chaku = [f1_row.row1 for f1_row in f1_chaku]

        f2_row_ippan = [f2_row.row1 for f2_row in f2_ippan]
        f2_row_cameko = [f2_row.row1 for f2_row in f2_cameko]
        f2_row_josei = [f2_row.row1 for f2_row in f2_josei]
        f2_row_chaku = [f2_row.row1 for f2_row in f2_chaku]

        f3_row_ippan = [f3_row.row1 for f3_row in f3_ippan]
        f3_row_cameko = [f3_row.row1 for f3_row in f3_cameko]
        f3_row_josei = [f3_row.row1 for f3_row in f3_josei]
        f3_row_chaku = [f3_row.row1 for f3_row in f3_chaku]

        f4_row_ippan = [f4_row.row1 for f4_row in f4_ippan]
        f4_row_cameko = [f4_row.row1 for f4_row in f4_cameko]
        f4_row_josei = [f4_row.row1 for f4_row in f4_josei]
        f4_row_chaku = [f4_row.row1 for f4_row in f4_chaku]

        ticketchart = graph.ticketchart(ticket,ticketsval)
        sheetchart = graph.sheetratio(sheet)
        floorchart = graph.floorchart(floor,floorsval)

        f1_histgram = graph.Floor_Histogram(f1_row_ippan,f1_row_cameko,f1_row_josei,f1_row_chaku)
        f2_histgram = graph.Floor_Histogram(f2_row_ippan,f2_row_cameko,f2_row_josei,f2_row_chaku)
        f3_histgram = graph.Floor_Histogram(f3_row_ippan,f3_row_cameko,f3_row_josei,f3_row_chaku)
        f4_histgram = graph.Floor_Histogram(f4_row_ippan,f4_row_cameko,f4_row_josei,f4_row_chaku)
       # heatmap = graph.Arena_HeatMap(block,column,arenasheet,rowmax,columnmax)
        heatmap2 = graph.Floor_HeatMap(row,number,arenasheet,rowmax,columnmax)
        
        performcount = performtimes.count()
        ctx['ticketchart'] = ticketchart
        ctx['sheetchart'] = sheetchart
        ctx['floorchart'] = floorchart

        ctx['f1_histgram'] = f1_histgram
        ctx['f2_histgram'] = f2_histgram
        ctx['f3_histgram'] = f3_histgram
        ctx['f4_histgram'] = f4_histgram

        ctx['heatmap'] = heatmap2
       # ctx['sheetratio1'] = sheetratio1
        ctx['results'] = qs
        ctx['title'] = venuemodel
        ctx['count'] = count
        ctx['num'] = self.kwargs['num']
        ctx['performcount'] = performcount
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
