from django.contrib import admin
from .models import Client, Gender, FindOut, Status, Ltv

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'father_name', 'get_gender_id', 'mobile_phone', 'iin', 'date_of_birth', 'get_find_out_id', 'created_at', 'updated_at')
    
    def get_gender_id(self, obj):
        return obj.gender.id
    
    def get_find_out_id(self, obj):
        return obj.find_out.id
    
    get_gender_id.short_description = 'Gender ID'
    get_find_out_id.short_description = 'Find Out ID'

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender_name')

@admin.register(FindOut)
class FindOutAdmin(admin.ModelAdmin):
    list_display = ('id', 'find_out_name')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')

@admin.register(Ltv)
class LTVAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'services', 'status', 'specalization_title', 
        'tooth', 'specalization_cost', 'count', 'total', 
        'created_at', 'updated_at'
    )
    search_fields = (
        'client__name', 'services__title', 'status__title', 
        'specalization_title__title'
    )
    list_filter = (
        'created_at', 'updated_at', 'status', 
        'specalization_title'
    )