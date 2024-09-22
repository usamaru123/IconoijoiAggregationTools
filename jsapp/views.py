from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView,TemplateView
from django.contrib.auth.views import LoginView
from .models import MenberModel,EventModel,VenueModel,HallTypeModel,HallInfoModel,TicketTypeModel,m_contact_typ,t_contact,t_answer
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from matplotlib import pyplot as plt
from . import graph 
import csv,urllib
import datetime
from django.db.models import Q

from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin




import logging


logger = logging.getLogger(__name__)


class Toppage(ListView): #トップページ
    template_name = 'index.html'
    model = EventModel

    def get_context_data(self,*args,**kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = VenueModel.objects.order_by('venuedateFROM').all()
        return ctx
    
class Adminpage(LoginRequiredMixin,ListView): #トップページ
    template_name = 'admin.html'
    model = EventModel

    def get_context_data(self,*args,**kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = VenueModel.objects.order_by('venuedateFROM').all()
        return ctx


class AnswerList(ListView): #回答一覧ページ
    template_name = 'result.html'
    model = EventModel


    def get_context_data(self,*args,**kwargs,):

        ctx = super().get_context_data(**kwargs)
        qsmodel = MenberModel.objects.filter(venueid=self.kwargs['num']).all()
        venuemodel = VenueModel.objects.get(venueid=self.kwargs['num'])

        performtimes = venuemodel.perform_time.order_by('disp_priority')
        floorvalobj = venuemodel.floor.order_by('priority')
        sheetvalobj = venuemodel.sheettype.order_by('priority')

        floorsval = [floor.floorname for floor in floorvalobj]
        sheetsval = [sheet.sheet for sheet in sheetvalobj]


        time = 'matinee'
        

        if(time):
            time = self.request.GET.get('time')

        count = qsmodel.count()

           
        if time == 'evening':
            qs = qsmodel.exclude(ticket2__exact="")

        else:
            qs = qsmodel.exclude(ticket1__exact="")


        results = qs.order_by("timedate").reverse()[0:100]
        
        performcount = performtimes.count()


       # ctx['sheetratio1'] = sheetratio1
        ctx['results'] = results
        ctx['title'] = venuemodel
        ctx['count'] = count
        ctx['num'] = self.kwargs['num']
        ctx['performcount'] = performcount
        ctx['performtimes'] = performtimes
        ctx['floorsval'] = floorsval
        ctx['sheetsval'] = sheetsval

        return  ctx

class AnswerCreate(CreateView): #回答作成フォーム
    template_name = 'create2.html'
    model = MenberModel
    
    fields = ('venueid','matinee','evening','sale1','ticket1','sheet1','floor1','row1','block_r1','block_c1','number1','sale2','ticket2','sheet2','floor2','row2','block_r2','block_c2','number2',)
    def get_context_data(self,*args,**kwargs,):
        ctx = super().get_context_data(**kwargs)
        answerObj =  MenberModel.objects.filter(venueid=self.kwargs['num']).all()
        venueObj = VenueModel.objects.get(venueid=self.kwargs['num'])
        performtimes = venueObj.perform_time.order_by('disp_priority')
        hall = venueObj.hall.order_by('priority')
        floor = venueObj.floor.order_by('priority')
        sheets = venueObj.sheettype.order_by('priority')
        sales = venueObj.salestype.order_by('priority')


        c_answer = answerObj.count()
        

        ctx['count'] = c_answer
        ctx['title'] = venueObj
        ctx['results'] = answerObj
        ctx['blocks'] = hall
        ctx['floors'] = floor
        ctx['sheets'] = sheets
        ctx['performtimes'] = performtimes
        ctx['sales'] = sales
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
        ctx['venue'] = VenueModel.objects.order_by('venuedateFROM')
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
    

class ContactCreate(CreateView):
    template_name = 'contact_create.html'
    model = t_contact

    fields=  ('nam', 'contact_text','email')
    success_url = ("contact-thanks")

class ContactThanks(TemplateView):
    template_name = 'contact_thanks.html'

class ContactList(LoginRequiredMixin,ListView):
    template_name = 'contact_list.html'
    model = t_contact

class PrivacyPolicy(TemplateView):
    template_name = 'privacy_policy.html'

class Login(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

    
def csv_export(request,num):
    No = 1
    response = HttpResponse(content_type='text\csv; charset=Shift-JIS')
    now = datetime.datetime.now()
    downloadtime = now.strftime('%Y%m%d_%H%M%S')
    f = str(num) + '集計結果：' + downloadtime +  '.csv'
    header = [
        'No.',
        '日時',
        '昼販売',
        '昼チケット',
        '昼座席',
        '昼フロア',
        '昼縦ブロック',
        '昼横ブロック',
        '昼列',
        '昼番号',
        '夜販売',
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
            result.sale1,
            result.ticket1,
            result.sheet1,
            result.floor1,
            result.block_r1,
            result.block_c1,
            result.row1,
            result.number1,
            result.sale2,
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

