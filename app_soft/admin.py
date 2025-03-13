from django.contrib import admin
from app_soft.models import *

# Register your models here.
admin.site.register(Article)
admin.site.register(Games)


admin.site.site_header = "Panel zarządzania grami"
admin.site.site_title = "Panel Admina"
admin.site.index_title = "Zarządzanie grami"