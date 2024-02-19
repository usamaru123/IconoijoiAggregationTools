from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import MenberModel,EventModel,VenueModel
from django.urls import reverse_lazy
from django.http import HttpResponse



class AnswerList(ListView):
    template_name = 'index.html'
    model = MenberModel
    def get_context_data(self,*args,**kwargs,):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = VenueModel.objects.get(venueid=self.kwargs['num'])
        return  ctx

class AnswerCreate(CreateView):
    template_name = 'create2.html'
    model = MenberModel

    fields = ('eventtitle','venue','matinee','evening','ticket1','sheet1','floor1','block1','number1','ticket2','sheet2','floor2','block2','number2',)


    success_url = reverse_lazy('index')


class EventCreate(CreateView):
    template_name = 'event.html'
    model = EventModel
    fields =('eventid','group','eventtype','eventtitle')
    success_url = ('eventlist')
   
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
    success_url = ('venuelist')

class VenueList(ListView):
    model = EventModel
    template_name = 'venuelist.html'
    def get_context_data(self,*args,**kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['venue'] = VenueModel.objects.order_by('venuedate')
        return ctx
