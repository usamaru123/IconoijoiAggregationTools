from django.urls import path
from .views import Toppage,AnswerList,AnswerCreate,EventCreate,EventList,VenueCreate,VenueList,ThanksView,csv_export,HallinfoCreate,Adminpage,ContactCreate,ContactThanks,PrivacyPolicy,ContactList,Login

app_name = 'jsapp'

urlpatterns = [
    path('',Toppage.as_view(),name='toppage'),
    path('admin_page',Adminpage.as_view(),name='adminpage'),
    path('result/<int:num>',AnswerList.as_view(),name='index'),
    path('<int:num>/',AnswerCreate.as_view(),name='create'),
    path('eventcreate',EventCreate.as_view(),name='eventcreate'),
    path('hallcreate',HallinfoCreate.as_view(),name='hallinfocreate'),
    path('eventlist',EventList.as_view(),name='eventlist'),
    path('venuecreate',VenueCreate.as_view(),name='venuecreate'),
    path('venuelist',VenueList.as_view(),name='venuelist'),
    path('results/<int:num>',ThanksView.as_view(),name='thanks'),
    path('export/<int:num>',csv_export,name=("export")),
    path('contactform',ContactCreate.as_view(),name='contactcreate'),
    path('contact-thanks',ContactThanks.as_view(),name='contact_thanks'),
    path('privacy-policy',PrivacyPolicy.as_view(),name='privacy_policy'),
    path('contact-list',ContactList.as_view(),name='contact_list'),
    path('login/',Login.as_view(),name='login'),
]
