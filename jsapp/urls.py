from django.urls import path
from .views import index,AnswerCreate

urlpatterns = [
    path('main/',index,name='index'),
    path('ikolove/2024/tour/2/',AnswerCreate.as_view(),name='create')
]
