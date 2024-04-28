from django.urls import path
from .views import Toppage,AnswerList,AnswerCreate,EventCreate,EventList,VenueCreate,VenueList,ThanksView,csv_export,HallinfoCreate

app_name = 'jsapp'

urlpatterns = [
    path('admin_page',Toppage.as_view(),name='toppage'),
    path('result/<int:num>',AnswerList.as_view(),name='index'),
    path('<int:num>/',AnswerCreate.as_view(),name='create'),
    path('eventcreate',EventCreate.as_view(),name='eventcreate'),
    path('hallcreate',HallinfoCreate.as_view(),name='hallinfocreate'),
    path('eventlist',EventList.as_view(),name='eventlist'),
    path('venuecreate',VenueCreate.as_view(),name='venuecreate'),
    path('venuelist',VenueList.as_view(),name='venuelist'),
    path('results/<int:num>',ThanksView.as_view(),name='thanks'),
    path('export/<int:num>',csv_export,name=("export")),
]
