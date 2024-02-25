from django.contrib import admin
from .models import MenberModel,EventModel,VenueModel,HallInfo
# Register your models here.
admin.site.register(MenberModel)
admin.site.register(EventModel)
admin.site.register(VenueModel)
admin.site.register(HallInfo)