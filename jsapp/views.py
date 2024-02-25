from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import MenberModel,EventModel,VenueModel
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect
from matplotlib import pyplot as plt
from . import graph

class AnswerList(ListView):
    template_name = 'index.html'
    model = EventModel
    def get_context_data(self,*args,**kwargs,):
        ctx = super().get_context_data(**kwargs) 
        qs = MenberModel.objects.filter(venueid=self.kwargs['num'],floor1='アリーナ席').all()
        row = [row.block_r1 for row in qs]
        column = [number.block_c1 for number in qs]
        sheet = [sheet.sheet1 for sheet in qs ]

        chart = graph.Arena_HeatMap(row,column,sheet)
        ctx['chart'] = chart
        ctx['results'] = MenberModel.objects.filter(venueid=self.kwargs['num']).all()
        ctx['title'] = VenueModel.objects.get(venueid=self.kwargs['num'])
        return  ctx

class AnswerCreate(CreateView):
    template_name = 'create2.html'
    model = MenberModel
    
    fields = ('venueid','matinee','evening','ticket1','sheet1','floor1','row1','block_r1','block_c1','number1','ticket2','sheet2','floor2','row2','block_r2','block_c2','number2',)
    def get_context_data(self,*args,**kwargs,):
        ctx = super().get_context_data(**kwargs)
        answerObj =  MenberModel.objects.filter(venueid=self.kwargs['num']).all()
        venueObj = VenueModel.objects.get(venueid=self.kwargs['num'])
        blocks = venueObj.hallinfo.halltype
        c_answer = answerObj.count()
        

        ctx['count'] = c_answer
        ctx['title'] = venueObj
        ctx['results'] = answerObj
        ctx['blocks'] = blocks
        return  ctx

    def get_success_url(self):
        return reverse_lazy('thanks',kwargs={"num":self.kwargs['num']})


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


class ThanksView(ListView):
    template_name = 'thanks.html'
    model = EventModel
    def get_context_data(self,*args,**kwargs,):
        ctx = super().get_context_data(**kwargs)
        ctx['results'] = MenberModel.objects.filter(venueid=self.kwargs['num']).all()
        ctx['title'] = VenueModel.objects.get(venueid=self.kwargs['num'])
        return  ctx