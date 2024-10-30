from django.contrib import admin
from .models import Service, Appointment

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')  # Ensure 'duration' exists in Service model

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'date', 'time_slot', 'status')  # Ensure 'client' and 'status' exist in Appointment model

admin.site.register(Service, ServiceAdmin)
admin.site.register(Appointment, AppointmentAdmin)
