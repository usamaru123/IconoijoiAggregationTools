from django.urls import path
from .views import AnswerList,AnswerCreate,EventCreate,EventList,VenueCreate,VenueList,ThanksView

urlpatterns = [
    path('20240301/',AnswerList.as_view(),name='index'),
    path('result/<int:num>',AnswerList.as_view(),name='index'),
    path('<int:num>/',AnswerCreate.as_view(),name='create'),
    path('eventcreate',EventCreate.as_view(),name='eventcreate'),
    path('eventlist',EventList.as_view(),name='eventlist'),
    path('venuecreate',VenueCreate.as_view(),name='venuecreate'),
    path('venuelist',VenueList.as_view(),name='venuelist'),
    path('results/<int:num>',ThanksView.as_view(),name='thanks')
]
