from django.contrib import admin
from .models import Branche, User, Agency

# Register your models here.
admin.site.register(User)
admin.site.register(Agency)
admin.site.register(Branche)