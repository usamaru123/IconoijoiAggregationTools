from django.urls import path
from .views import index,AnswerForm

urlpatterns = [
    path('main/',index,name='index'),
    path('',AnswerForm.as_view(),name='create')
]
