from django.contrib import admin
from agencies.models import Bus, Bus_layout, Trip

# Register your models here.
admin.site.register(Bus_layout)
admin.site.register(Bus)
admin.site.register(Trip)