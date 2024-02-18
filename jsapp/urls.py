from django.urls import path
from .views import index,AnswerCreate,EventCreate,EventList,VenueCreate,VenueList

urlpatterns = [
    path('main/',index,name='index'),
    path('ikolove/<int:num>/',AnswerCreate.as_view(),name='create'),
    path('eventcreate',EventCreate.as_view(),name='eventcreate'),
    path('eventlist',EventList.as_view(),name='eventlist'),
    path('venuecreate',VenueCreate.as_view(),name='venuecreate'),
    path('venuelist',VenueList.as_view(),name='venuelist'),
]
