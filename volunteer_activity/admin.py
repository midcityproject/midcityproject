from django.contrib import admin
from .models import User, Event, UserEvent

#class UserList(admin.ModelAdmin):
 #   list_display = ('user_number', 'name', 'city', 'cell_phone')
  #  list_filter = ('user_number', 'name', 'city')
   # search_fields = ('user_number', 'name')
    #ordering = ['hours_volunteered']

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


#admin.site.register(User, UserList)
admin.site.register(Event, EventList)
admin.site.register(UserEvent, UserEventList)

