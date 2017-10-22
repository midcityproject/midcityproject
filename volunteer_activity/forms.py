from django import forms
from .models import User, Event, UserEvent


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'city', 'state', 'hours_volunteered', )


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('organization', 'type', 'location', 'description', 'start_date', 'end_date', 'time', 'number_volunteers',)

class UserEventForm(forms.ModelForm):
    class Meta:
        model = UserEvent
        fields = ('event_num', 'date', 'hours', )