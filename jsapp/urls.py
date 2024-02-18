from django.urls import path
from .views import index,AnswerCreate,EventCreate,Eventlist

urlpatterns = [
    path('main/',index,name='index'),
    path('ikolove/2024/tour/2/',AnswerCreate.as_view(),name='create'),
    path('eventcreate',EventCreate.as_view(),name='eventcreate'),
    path('eventlist',Eventlist.as_view(),name='eventlist'),
]
