from django.db import models
from django.utils import timezone
# Create your models here.
class MenberModel(models.Model):
   datetime = models.DateTimeField(auto_now_add=True)
   title = models.CharField(max_length=100,blank=True)
   venue = models.CharField(max_length=100,blank=True)

   matinee = models.BooleanField(default=False)
   evening = models.BooleanField(default=False)

   ticket1 = models.CharField(max_length=100,blank=True)
   sheet1 = models.CharField(max_length=100,blank=True)
   floor1 = models.CharField(max_length=100,blank=True)
   block1 = models.CharField(max_length=100,blank=True)
   number1 = models.CharField(max_length=100,blank=True)

   ticket2 = models.CharField(max_length=100,blank=True)
   sheet2 = models.CharField(max_length=100,blank=True)
   floor2 = models.CharField(max_length=100,blank=True)
   block2 = models.CharField(max_length=100,blank=True)
   number2 = models.CharField(max_length=100,blank=True)