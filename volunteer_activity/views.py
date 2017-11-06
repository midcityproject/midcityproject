
from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
#from .forms import *
from django.db.models import Sum


def home(request):
    users = User.objects.all()
    events = Event.objects.all()
    return render(request, 'volunteer_activity/home.html',
                  {'volunteer_activity': home, 'users': users, 'events': events, })

def aboutus(request):
   return render(request, 'volunteer_activity/aboutus.html',
                 {'volunteer_activity': aboutus})

def manage_activity(request):
   return render(request, 'volunteer_activity/manage_activity.html',
                 {'volunteer_activity': manage_activity})

def register(request):
   return render(request, 'volunteer_activity/register.html',
                 {'volunteer_activity': register})

def contactus(request):
   return render(request, 'volunteer_activity/contactus.html',
                 {'volunteer_activity': contactus})

def events(request):
    events = Event.objects.all()
    return render(request, 'volunteer_activity/events.html',
                 {'volunteer_activity': events, 'events': events, })

def tracking(request):
    userevents = UserEvent.objects.all()
    return render(request, 'volunteer_activity/tracking.html',
                 {'volunteer_activity': tracking, 'userevents': userevents,})

def event_details(request):
   return render(request, 'volunteer_activity/event_details.html',
                 {'volunteer_activity': event_details,})

def signup(request):
   return render(request, 'volunteer_activity/signup.html',
                 {'volunteer_activity': signup})

def add_event(request):
   return render(request, 'volunteer_activity/add_event.html',
                 {'volunteer_activity': add_event})

def edit_event(request):
   return render(request, 'volunteer_activity/edit_event.html',
                 {'volunteer_activity': edit_event})

def pwd_recover(request):
   return render(request, 'volunteer_activity/pwd_recover.html',
                 {'volunteer_activity': pwd_recover})
