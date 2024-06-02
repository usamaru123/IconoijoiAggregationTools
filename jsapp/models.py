from django.db import models
from django.utils import timezone
# Create your models here.
class GroupModel(models.Model): #グループ情報を保存するマスタです
   group = models.CharField(max_length=100)
   def __str__(self):
      return self.group
   
class EventTypeModel(models.Model): #イベントの属性を保存するマスタです
   eventtypeid = models.IntegerField(primary_key=True)
   eventtype = models.CharField(max_length=100)
   def __str__(self):
      return str(self.eventtypeid) +'.' + self.eventtype

class EventModel(models.Model):  #イベントの情報を保存するマスタです
   eventid = models.IntegerField(primary_key=True)
   eventtype = models.ForeignKey(EventTypeModel,on_delete=models.CASCADE)
   group = models.ManyToManyField(GroupModel,default=[1])
   eventtitle = models.CharField(max_length=100)
   def __str__(self):
      return str(self.eventid) + "."+ self.eventtitle
   

class TicketSheetMaster(models.Model):
   priority = models.IntegerField()
   sheet = models.CharField(max_length = 10)
   def __str__(self):
      return str(self.priority) + "." + self.sheet

class SheetValMaster(models.Model): #座席の入力規則を保存するマスタです
   valid = models.IntegerField(primary_key=True)
   valname = models.CharField(max_length=100)
   pattern = models.TextField()
   def __str__(self):
      return str(self.valid) + "." + self.valname

class SheetModel(models.Model): #座席の属性を保存するマスタです
   priority = models.IntegerField()
   sheetname = models.CharField(max_length=100)
   prename = models.CharField(max_length=10,blank=True)
   postname = models.CharField(max_length=10,blank=True)
   sheettype = models.ForeignKey(SheetValMaster,on_delete=models.CASCADE)
   def __str__(self):
      return str(self.priority) + "." + self.sheetname + ": " + self.prename +  self.sheettype.valname +  self.postname 
   
class HallTypeDtlModel(models.Model):
  typeid = models.IntegerField(default=1,primary_key=True)
  typename = models.CharField(max_length=10)
  def __str__(self):
     return str(self.typeid) + "." + self.typename
  


class HallTypeModel(models.Model): #会場の属性を保存するマスタです
   priority = models.IntegerField(default = 1)
   identname = models.CharField(max_length =100)
   hallval = models.ForeignKey(HallTypeDtlModel,on_delete=models.CASCADE)
   blockname = models.CharField(max_length=100)
   sheets = models.ManyToManyField(SheetModel,default=[1])
   def __str__(self):
      return  str(self.priority) + "." + self.blockname + "." + self.identname
   
class HallSetModel(models.Model):
   setid = models.IntegerField(default=1)
   setname = models.CharField(max_length=10)
   hallset = models.ManyToManyField(HallTypeModel,default=[1])

class HallInfoModel(models.Model): #会場の情報を保存するマスタです
   hallid = models.IntegerField(primary_key=True)
   hallname = models.CharField(max_length=100)
   hallprefecture = models.CharField(max_length=100)
   def __str__(self):
      return str(self.hallid) + "." + self.hallname
   

class TicketTypeModel(models.Model):
   priority = models.IntegerField()
   tickettype = models.CharField(max_length=100)
   def __str__(self):
      return str(self.priority) + "." + self.tickettype

class m_PerformTime(models.Model): #公演時間を保存するマスタです
   disp_priority = models.IntegerField()
   perform_time = models.CharField(max_length=100)
   def __str__(self):
      return str(self.disp_priority) + "." + self.perform_time

class VenueModel(models.Model): #公演の情報を保存するフィールドです
   venueid = models.IntegerField(primary_key=True)
   venuedate = models.DateField()
   event = models.ForeignKey(EventModel,on_delete=models.CASCADE)
   rowmax = models.IntegerField(default=1,blank=True)
   columnmax = models.IntegerField(default=1,blank=True)
   hallinfo = models.ForeignKey(HallInfoModel,on_delete=models.CASCADE,default=1)
   perform_time = models.ManyToManyField(m_PerformTime,default="")
   tickettype = models.ManyToManyField(TicketTypeModel,default="")
   sheettype = models.ManyToManyField(TicketSheetMaster,default="")
   hallset = models.ForeignKey(HallSetModel,on_delete=models.CASCADE,default=1)

   def __str__(self):
      return str(self.venueid) + "." + self.event.eventtitle + self.hallinfo.hallname 

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

   def __str__(self):
      return "id:"+ str(self.id) + ",timedate" + str(self.timedate)

