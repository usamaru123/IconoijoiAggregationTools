from django.db import models
from django.utils import timezone
# Create your models here.
class EventModel(models.Model):
   eventid = models.IntegerField(primary_key=True)
   group = models.CharField(max_length=10)
   eventtype = models.CharField(max_length=10)
   eventtitle = models.CharField(max_length=100,)

   def __str__(self):
      return self.eventtitle
   
class HallInfoModel(models.Model):
   hallname = models.CharField(max_length=100,primary_key=True)
   halltype = models.CharField(max_length=100)
   floor = models.IntegerField()
   blocks = models.IntegerField(blank=True)
   rows = models.IntegerField(blank=True)
   numbers = models.BigIntegerField()
   prefecture = models.CharField(max_length=100)
      
class VenueModel(models.Model):
   venueid = models.IntegerField(primary_key=True)
   venuedate = models.DateField()
   event = models.ForeignKey(EventModel,on_delete=models.CASCADE)
   prefecture = models.CharField(max_length=10)
   venue = models.CharField(max_length=100)
   hallinfo = models.ForeignKey(HallInfoModel,on_delete=models.CASCADE)

   def __str__(self):
      return self.venue

class MenberModel(models.Model):
   venueid = models.IntegerField(blank=True)
   timedate = models.DateTimeField(default=timezone.now)

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



   def __str__(self):
      return self.hallname

