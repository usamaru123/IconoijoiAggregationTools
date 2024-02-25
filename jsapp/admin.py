from django.contrib import admin
from .models import MenberModel,EventModel,VenueModel,HallInfoModel,HallTypeModel
# Register your models here.
admin.site.register(MenberModel)
admin.site.register(EventModel)
admin.site.register(VenueModel)
admin.site.register(HallInfoModel)
admin.site.register(HallTypeModel)