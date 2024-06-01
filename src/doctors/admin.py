from django.contrib import admin
from .models import Specialization, Service, Doctors, Assistant, DoctorClient

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'spec_id', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('spec_id', 'created_at',)

@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'father_name', 'services_id', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'father_name')
    list_filter = ('services_id', 'created_at',)

@admin.register(Assistant)
class AssistantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'father_name', 'services_id', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'father_name')
    list_filter = ('services_id', 'created_at',)

@admin.register(DoctorClient)
class DoctorClientAdmin(admin.ModelAdmin):
    list_display = ('doctor_id', 'client_id', 'id')
    search_fields = ('doctor_id__first_name', 'doctor_id__last_name', 'client_id__first_name', 'client_id__last_name')
    list_filter = ('doctor_id', 'client_id')
