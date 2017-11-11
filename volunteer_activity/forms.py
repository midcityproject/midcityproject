from django import forms
from .models import User, Profile, Event, UserEvent

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'address', 'city', 'state', 'zipcode', 'cell_phone', 'active_inactive', 'created_date',)

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('organization', 'type', 'location', 'short_description', 'description', 'start_date', 'time', 'number_volunteers',)


class UserEventForm(forms.ModelForm):
    class Meta:
        model = UserEvent
        fields = ('event_num', 'hours',)