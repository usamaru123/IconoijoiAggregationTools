from django.urls import path
from .views import index,AnswerCreate,EventCreate,EventList

urlpatterns = [
    path('main/',index,name='index'),
    path('ikolove/2024/tour/2/',AnswerCreate.as_view(),name='create'),
    path('eventcreate',EventCreate.as_view(),name='eventcreate'),
    path('eventlist',EventList.as_view(),name='eventList'),
]
