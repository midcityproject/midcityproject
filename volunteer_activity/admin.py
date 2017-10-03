from django.contrib import admin
from .models import User, Event

class UserList(admin.ModelAdmin):
    list_display = ('user_number', 'name', 'city', 'cell_phone')
    list_filter = ('user_number', 'name', 'city')
    search_fields = ('user_number', 'name')
    ordering = ['user_number']

class EventList(admin.ModelAdmin):
    list_display = ('volunteer', 'type', 'location', 'description')
    list_filter = ('volunteer', 'type')
    search_fields = ('volunteer', 'type')
    ordering = ['volunteer']


admin.site.register(User, UserList)
admin.site.register(Event, EventList)

