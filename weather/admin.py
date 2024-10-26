# admin.py
from django.contrib import admin
from .models import TemperatureRecord  # Import your model

@admin.register(TemperatureRecord)
class TemperatureRecordAdmin(admin.ModelAdmin):
    list_display = ('city', 'temperature', 'recorded_at')  # Columns to display in the admin list view
    search_fields = ('city',)  # Allow searching by city

# If you have another model like CityWeather, register it similarly
