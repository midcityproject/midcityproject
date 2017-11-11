from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Sum

def home(request):
    userevents = UserEvent.objects.filter(user_num=request.user.pk).order_by('-event_num')[:5]
    events = Event.objects.all().order_by('-start_date')[:5]
    return render(request, 'volunteer_activity/home.html',
                  {'volunteer_activity': home, 'events': events, 'userevents': userevents,})

def aboutus(request):
   return render(request, 'volunteer_activity/aboutus.html',
                 {'volunteer_activity': aboutus})

def manage_activity(request):
    users = User.objects.all()
    userevents = UserEvent.objects.all()
    return render(request, 'volunteer_activity/manage_activity.html',
                 {'volunteer_activity': manage_activity, 'users': users,'userevents': userevents, })

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
@login_required
def tracking(request):
    userevents = UserEvent.objects.filter(user_num=request.user.pk)
    return render(request, 'volunteer_activity/tracking.html',
                 {'volunteer_activity': tracking, 'userevents': userevents, })
@login_required
def tracking_edit(request, pk):
    userevents= get_object_or_404(UserEvent, pk=pk)
    if request.method == "POST":
        # update
        form = UserEventForm(request.POST, instance=userevents)

        if form.is_valid():
            userevents = form.save(commit=False)
            #userevents.updated_date = timezone.now()
            userevents.save()
            #userevents = UserEvent.objects.filter(created_date__lte=timezone.now())
            userevents = UserEvent.objects.filter(user_num=request.user.pk)
            return render(request, 'volunteer_activity/tracking.html',
                {'volunteer_activity': tracking, 'userevents': userevents,})
    else:
        # edit
        form = UserEventForm(instance=userevents)
    return render(request, 'volunteer_activity/tracking_edit.html', {'form': form})


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
