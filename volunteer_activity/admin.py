from django.contrib import admin
from .models import Profile, Event, UserEvent


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'state', 'zipcode', 'cell_phone', 'active_inactive', 'created_date', )

class EventList(admin.ModelAdmin):
    list_display = ('event_num', 'type', 'location', 'description')
    list_filter = ('event_num', 'type')
    search_fields = ('event_num', 'type')
    ordering = ['start_date']

class UserEventList(admin.ModelAdmin):
    list_display = ('event_num', 'user_num', 'hours',)
    list_filter = ('event_num', )
    search_fields = ('event_num', )
    ordering = ['event_num']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Event, EventList)
admin.site.register(UserEvent, UserEventList)

