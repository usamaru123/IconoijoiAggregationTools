from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import MenberModel
from django.urls import reverse_lazy

def index(request):
    context = {
        'title': '＝LOVEアリーナツアー2024 「Tell me what\'s more than \"LOVE\"」',
        'venue': '東京公演'
    }
    
    return render(request,'index.html',context)
# Create your views here.



class AnswerForm(CreateView):
    template_name = 'create2.html'
    model = MenberModel
    fields = ('matinee','evening','ticket1','sheet1','floor1','block1','number1','ticket2','sheet2','floor2','block2','number2',)

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = '＝LOVEアリーナツアー2024 「Tell me what\'s more than \"LOVE\"」'
        context['venue'] =  '東京公演'
        return context
    

    success_url = reverse_lazy('index')
