from django.db import models
from django.utils import timezone
# Create your models here.
class MenberModel(models.Model):
   timedate = models.DateTimeField(default=timezone.now)
   eventtitle = models.CharField(max_length=100,blank=True)
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

class EventModel(models.Model):
   eventid = models.IntegerField(primary_key=True)
   group = models.CharField(max_length=10)
   eventtype = models.CharField(max_length=10)
   eventtitle = models.CharField(max_length=100)




   def __str__(self):
      return self.eventtitle
   
      
class VenueModel(models.Model):
   event = models.ForeignKey(EventModel,on_delete=models.CASCADE)
   prefecture = models.CharField(max_length=10)
