from django.db import models
from django.utils import timezone
# Create your models here.
class EventModel(models.Model):  #イベントの情報を保存するマスタです
   eventid = models.IntegerField(primary_key=True)
   group = models.CharField(max_length=10)
   eventtype = models.CharField(max_length=10)
   eventtitle = models.CharField(max_length=100,)

   def __str__(self):
      return self.eventtitle

class SheetValMaster(models.Model):
   valid = models.IntegerField(primary_key=True)
   valname = models.CharField(max_length=100)
   def __str__(self):
      return self.valname

class SheetModel(models.Model): #座席の属性を保存するマスタです
   priority = models.IntegerField()
   sheetname = models.CharField(max_length=100)
   prename = models.CharField(max_length=10,blank=True)
   postname = models.CharField(max_length=10,blank=True)
   sheettype = models.ForeignKey(SheetValMaster,on_delete=models.CASCADE)
   def __str__(self):
      return self.sheetname + ",pre:" + self.prename + ",post:" + self.postname + self.sheettype.valname

class HallTypeModel(models.Model): #会場の属性を保存するマスタです
   priority = models.IntegerField(default = 1)
   halltype = models.CharField(max_length=100)
   blockname = models.CharField(max_length=100)
   sheet = models.ManyToManyField(SheetModel,default=1)
   def __str__(self):
      return self.blockname
   
   
class HallInfoModel(models.Model): #会場の情報を保存するマスタです
   hallid = models.IntegerField(primary_key=True)
   hallname = models.CharField(max_length=100)
   hallprefecture = models.CharField(max_length=100)
   halltype = models.ManyToManyField(HallTypeModel,default=1)
   def __str__(self):
      return self.hallname
   



class m_PerformTime(models.Model): #公演時間を保存するマスタです
   disp_priority = models.IntegerField()
   perform_time = models.CharField(max_length=100)
   def __str__(self):
      return self.perform_time

class VenueModel(models.Model): #公演の情報を保存するフィールドです
   venueid = models.IntegerField(primary_key=True)
   venuedate = models.DateField()
   event = models.ForeignKey(EventModel,on_delete=models.CASCADE)
   rowmax = models.IntegerField(default=1,blank=True)
   columnmax = models.IntegerField(default=1,blank=True)
   hallinfo = models.ForeignKey(HallInfoModel,on_delete=models.CASCADE,default=1)
   perform_time = models.ManyToManyField(m_PerformTime,default="")
   

   def __str__(self):
      return self.event.eventtitle + self.hallinfo.hallname 

class MenberModel(models.Model): #アンケート回答結果を保存するフィールドです
   answerid= models.BigIntegerField(blank=True,default=1)
   venueid = models.ForeignKey(VenueModel,blank=True,on_delete=models.CASCADE,default=20240301)
   timedate = models.DateTimeField(default=timezone.now)

   matinee = models.BooleanField(default=False)
   evening = models.BooleanField(default=False)

   ticket1 = models.CharField(max_length=100,blank=True)
   sheet1 = models.CharField(max_length=100,blank=True)
   floor1 = models.CharField(max_length=100,blank=True)
   row1 = models.CharField(max_length=100,blank=True)
   block_r1 = models.CharField(max_length=100,blank=True)
   block_c1 = models.CharField(max_length=100,blank=True)
   number1 = models.CharField(max_length=100,blank=True)

   ticket2 = models.CharField(max_length=100,blank=True)
   sheet2 = models.CharField(max_length=100,blank=True)
   floor2 = models.CharField(max_length=100,blank=True)
   row2 = models.CharField(max_length=100,blank=True)
   block_r2 = models.CharField(max_length=100,blank=True)
   block_c2 = models.CharField(max_length=100,blank=True)
   number2 = models.CharField(max_length=100,blank=True)

