from django.contrib import admin
from .models import ContactUs
# Register your models here.
class AdminTable(admin.ModelAdmin):
    list_display=['name','email','subject','message','date']

admin.site.register(ContactUs,AdminTable)
