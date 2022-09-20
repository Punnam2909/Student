from django.contrib import admin
from .models import *


# Register your models here.

class SinfoAdmin(admin.ModelAdmin):
    list_display=("id","Name","GPA")


admin.site.register(Sinfo,SinfoAdmin)