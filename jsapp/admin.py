from django.contrib import admin
from .models import MenberModel,EventModel,VenueModel,HallInfoModel,HallTypeModel,m_PerformTime,SheetModel,SheetValMaster,GroupModel,HallTypeDtlModel,EventTypeModel,TicketTypeModel,TicketSheetMaster,HallSetModel
# Register your models here.
admin.site.register(MenberModel)
admin.site.register(EventModel)
admin.site.register(VenueModel)
admin.site.register(HallInfoModel)
admin.site.register(HallTypeModel)
admin.site.register(m_PerformTime)
admin.site.register(SheetModel)
admin.site.register(SheetValMaster)
admin.site.register(GroupModel)
admin.site.register(HallTypeDtlModel)
admin.site.register(EventTypeModel)
admin.site.register(TicketTypeModel)
admin.site.register(TicketSheetMaster)
admin.site.register(HallSetModel)
#admin.site.register(FloorModel)
#admin.site.register(FloorSetModel)