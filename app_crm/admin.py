from django.contrib import admin
from .models import Record

# Register your models here.

class AdminRecor(admin.ModelAdmin):  
    #tres important list_display et list_filter
    #list_display rends les colonnes d'une table dans Admin django visible
    #list_filter Permet de creer une sorte de filter
    #class admin.ModelAdmin Permet de personaliser admin django qui est un site
    list_display = ('pk', 'first_name', 'last_name', 'email', 'phone', 'adress')
    list_filter  = ('created_at',) 
admin.site.register(Record, AdminRecor)