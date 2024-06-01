from django.contrib import admin
from .models import RecordsLog, ChairNum, RecordingType, PaymentType, PaymentState, Record

@admin.register(RecordsLog)
class RecordsLogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')

@admin.register(ChairNum)
class ChairNumAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')

@admin.register(RecordingType)
class RecordingTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')

@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')

@admin.register(PaymentState)
class PaymentStateAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'client_first_name', 'client_last_name', 'client_father_name', 
        'doctor', 'doctors_name', 'assistant', 'assistant_name', 
        'services', 'specalization_title', 'tooth', 'specalization_cost', 
        'count', 'sell', 'total', 'registration_date', 'record_start', 
        'record_end', 'recording_type', 'title', 'notes', 'reason', 
        'reception_day', 'chair', 'payment_type', 'payment_state', 
        'created_at', 'updated_at'
    )
    search_fields = (
        'client_first_name', 'client_last_name', 'client_father_name', 
        'doctors_name', 'assistant_name', 'title'
    )
    list_filter = (
        'registration_date', 'record_start', 'record_end', 
        'reception_day', 'created_at', 'updated_at'
    )
    
