from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import MenberModel,EventModel
from django.urls import reverse_lazy
from django.http import HttpResponse

def index(request):
    resultsTitle = '＝LOVEアリーナツアー2024 「Tell me what\'s more than \"LOVE\"」'
    results = MenberModel.objects.all()
    context = {
        'results':results,
    }   
    return render(request,'index.html',context)
# Create your views here.



class AnswerCreate(CreateView):
    template_name = 'create2.html'
    model = MenberModel

    fields = ('eventtitle','venue','matinee','evening','ticket1','sheet1','floor1','block1','number1','ticket2','sheet2','floor2','block2','number2',)
    def get_context_data(self,*args,**kwargs,):
        ctx = super().get_context_data(**kwargs)
        ctx['eventtitle'] = '＝LOVEアリーナツアー2024 「Tell me what\'s more than \"LOVE\"」'
        ctx['venue'] ='東京公演'
        return  ctx

    success_url = reverse_lazy('index')


class EventCreate(CreateView):
    template_name = 'event.html'
    model = EventModel
    fields =('eventid','group','eventtype','eventtitle')
    success_url = ('eventlist')
   
class EventList(ListView):
    template_name = 'eventlist.html'
    model = EventModel
    
