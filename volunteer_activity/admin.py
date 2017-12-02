from django.contrib import admin
from .models import Profile, Event, UserEvent
import csv
import datetime
from django.http import HttpResponse

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
        filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export Report to CSV'

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'state', 'zipcode', 'cell_phone', 'active_inactive', 'created_date', )
    actions = [export_to_csv]

class EventList(admin.ModelAdmin):
    list_display = ('event_num', 'type', 'location', 'description')
    list_filter = ('event_num', 'type')
    search_fields = ('event_num', 'type')
    ordering = ['start_date']
    actions = [export_to_csv]

class UserEventList(admin.ModelAdmin):
    list_display = ('event_num', 'user_num', 'hours',)
    list_filter = ('event_num', )
    search_fields = ('event_num', )
    ordering = ['event_num']
    actions = [export_to_csv]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Event, EventList)
admin.site.register(UserEvent, UserEventList)

###################


