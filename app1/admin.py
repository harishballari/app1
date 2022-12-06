from django.contrib import admin
from app1.models import Details

# Register your models here.


@admin.register(Details)
class Detailsadmin(admin.ModelAdmin):
    list_display =['id','cname']