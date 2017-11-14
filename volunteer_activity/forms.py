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

class UserEventEmployeeForm(forms.ModelForm):
    class Meta:
        model = UserEvent
        fields = ('user_num', 'event_num', 'hours',)

class UserEmployeeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
		
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']