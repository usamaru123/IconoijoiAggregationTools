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
   sheet = models.CharField(max_length = 30)
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
   
class FloorModel(models.Model):
   priority = models.IntegerField(default=1)
   floorname = models.CharField(max_length=10,blank=True)
   def __str__(self):
      return str(self.priority) +"."+self.floorname
   


class HallInfoModel(models.Model): #会場の情報を保存するマスタです
   hallid = models.IntegerField(primary_key=True)
   hallname = models.CharField(max_length=100)
   hallprefecture = models.CharField(max_length=100)
   def __str__(self):
      return str(self.hallid) + "." + self.hallname
   

class TicketTypeModel(models.Model):
   priority = models.IntegerField()
   tickettype = models.CharField(max_length=100)
   dispticketname = models.CharField(max_length=20)
   sheettype = models.ManyToManyField(TicketSheetMaster,default=[1,2,3,4])
   def __str__(self):
      return str(self.priority) + "." + self.tickettype
   

class SalesType(models.Model):
   priority = models.IntegerField(default=1)
   salestype = models.CharField(max_length=20,blank=True)
   dispsalesname = models.CharField(max_length=20)
   def __str__(self):
      return str(self.priority) + "." + self.salestype
   
class BlockType(models.Model): #１階席の座席集計種別を設定します
   id = models.IntegerField(primary_key=True)
   disp_blocktype = models.CharField(max_length=20)
   def __str__(self):
      return str(self.id) + "." + self.disp_blocktype
   

class m_PerformTime(models.Model): #公演時間を保存するマスタです
   disp_priority = models.IntegerField()
   perform_time = models.CharField(max_length=100)
   tickettype = models.ManyToManyField(TicketTypeModel,default=[1])
   def __str__(self):
      return str(self.disp_priority) + "." + self.perform_time

class VenueModel(models.Model): #公演の情報を保存するフィールドです
   venueid = models.IntegerField(primary_key=True)
   venuedateFROM = models.DateField()
   venuedateTO = models.DateField(blank=True,null=True)
   event = models.ForeignKey(EventModel,on_delete=models.CASCADE)
   rowmax = models.IntegerField(default=1,blank=True)
   columnmax = models.IntegerField(default=1,blank=True)
   hallinfo = models.ForeignKey(HallInfoModel,on_delete=models.CASCADE,default=1)
   perform_time = models.ManyToManyField(m_PerformTime,default="")
   salestype = models.ManyToManyField(SalesType,default="")
   sheettype = models.ManyToManyField(TicketSheetMaster,default="")
   blocktype = models.ForeignKey(BlockType,on_delete=models.CASCADE,default=1)
   #hallset = models.ForeignKey(HallSetModel,on_delete=models.CASCADE)
   #floorset = models.ForeignKey(FloorSetModel,on_delete=models.CASCADE)
   floor = models.ManyToManyField(FloorModel,default="")
   hall = models.ManyToManyField(HallTypeModel,default="")

   def __str__(self):
      return str(self.venueid) + "." + self.event.eventtitle + self.hallinfo.hallname 

class MenberModel(models.Model): #アンケート回答結果を保存するフィールドです
   answerid = models.BigIntegerField(blank=True,default=1)
   venueid = models.ForeignKey(VenueModel,blank=True,on_delete=models.CASCADE,default=20240301)
   timedate = models.DateTimeField(default=timezone.now)

   matinee = models.BooleanField(default=False)
   evening = models.BooleanField(default=False)

   sale1  = models.CharField(max_length=100,blank=True,default='1')
   ticket1 = models.CharField(max_length=100,blank=True)
   sheet1 = models.CharField(max_length=100,blank=True)
   floor1 = models.CharField(max_length=100,blank=True)
   row1 = models.CharField(max_length=100,blank=True)
   block_r1 = models.CharField(max_length=100,blank=True)
   block_c1 = models.CharField(max_length=100,blank=True)
   number1 = models.CharField(max_length=100,blank=True)

   sale2  = models.CharField(max_length=100,blank=True,default='1')
   ticket2 = models.CharField(max_length=100,blank=True)
   sheet2 = models.CharField(max_length=100,blank=True)
   floor2 = models.CharField(max_length=100,blank=True)
   row2 = models.CharField(max_length=100,blank=True)
   block_r2 = models.CharField(max_length=100,blank=True)
   block_c2 = models.CharField(max_length=100,blank=True)
   number2 = models.CharField(max_length=100,blank=True)

   def __str__(self):
      return "id:"+ str(self.id) + ",timedate" + str(self.timedate)



class m_contact_typ(models.Model):
   contact_typ = models.IntegerField(primary_key=True)
   contact_nam = models.CharField(max_length=30)

   def __str__(self):
      return str(self.contact_typ) + "_" + self.contact_nam


class t_answer(models.Model):
   answer_id = models.BigAutoField(primary_key=True)
   nam = models.CharField(max_length=100)
   answer_text = models.TextField(max_length=5000)
   datetime = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return str(self.answer_id) + "_" + self.answer_text

class t_contact(models.Model):
   contact_id = models.BigAutoField(primary_key=True)
   contact_typ = models.ForeignKey(m_contact_typ,on_delete=models.CASCADE,default=1)
   nam = models.CharField(max_length=100,blank=True)
   contact_text = models.TextField(max_length=5000)
   answer_id = models.ForeignKey(t_answer,on_delete=models.CASCADE,blank=True)
   venue_id = models.ForeignKey(VenueModel,on_delete=models.CASCADE,blank=True)
   disp_flg = models.IntegerField(default=1)
   datetime = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return str(self.contact_id) + "_" + self.contact_text