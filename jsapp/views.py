from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import MenberModel
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
    def get(self,request,*args,**kwargs):
        template_name = 'create2.html'
        model = MenberModel
        fields = ('title','venue','matinee','evening','ticket1','sheet1','floor1','block1','number1','ticket2','sheet2','floor2','block2','number2',)

        context = { 
            'title' : '＝LOVEアリーナツアー2024 「Tell me what\'s more than \"LOVE\"」',
            'venue' :  '東京公演'
        }

        return render(request,template_name,context)
    
    def post(self,request,*args,**kwargs):
        return render(request,'index.html',{'error':'投稿成功'})


