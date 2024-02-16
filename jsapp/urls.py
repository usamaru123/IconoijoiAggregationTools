from django.urls import path
from .views import index,AnswerForm

urlpatterns = [
    path('main/',index,name='index'),
    path('ikolove/2024/tour/2',AnswerForm.as_view(),name='create')
]
