from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Sum
from .models import Event
from django.views import generic


class IndexView(generic.ListView):
     template_name = 'volunteer_activity/events.html'
     model = Event

     def get_quereyset(self):
         return Event.objects.all()

class DetailView(generic.DetailView):
    model = Event
    template_name = 'volunteer_activity/event_details.html'

def home(request):
    userevents = UserEvent.objects.filter(user_num=request.user.pk).order_by('-event_num')[:5]
    events = Event.objects.all().order_by('-start_date')[:5]
    return render(request, 'volunteer_activity/home.html',
                  {'volunteer_activity': home, 'events': events, 'userevents': userevents,})

def aboutus(request):
   return render(request, 'volunteer_activity/aboutus.html',
                 {'volunteer_activity': aboutus})
######################### Manage Activity Page ######################
def manage_activity(request):
    users = User.objects.all()
    userevents = UserEvent.objects.all()
    events = Event.objects.all()
    return render(request, 'volunteer_activity/manage_activity.html',
                 {'volunteer_activity': manage_activity, 'users': users,'userevents': userevents, 'events': events,})

def volunteer_add(request):
    if request.method == "POST":
        form = UserEmployeeForm(request.POST)
        if form.is_valid():
            users = form.save(commit=False)
            users.save()
            users = User.objects.all()
            userevents = UserEvent.objects.all()
            events = Event.objects.all()
            return render(request, 'volunteer_activity/manage_activity.html',
                          {'volunteer_activity': manage_activity, 'users': users, 'userevents': userevents,
                           'events': events, })
    else:
        form = UserEmployeeForm()
        # print("Else")
    return render(request, 'volunteer_activity/volunteer_add.html', {'form': form})

def volunteer_edit(request, pk):
    users= get_object_or_404(User, pk=pk)
    if request.method == "POST":
        # update
        form = UserEmployeeForm(request.POST, instance=users)

        if form.is_valid():
            users = form.save(commit=False)
            #userevents.updated_date = timezone.now()
            users.save()
            #userevents = UserEvent.objects.filter(created_date__lte=timezone.now())
            #userevents = UserEvent.objects.filter(user_num=pk)
            users = User.objects.all()
            userevents = UserEvent.objects.all()
            events = Event.objects.all()
            return render(request, 'volunteer_activity/manage_activity.html',
                          {'volunteer_activity': manage_activity, 'users': users, 'userevents': userevents,
                           'events': events, })
    else:
        # edit
        form = UserEmployeeForm(instance=users)
    return render(request, 'volunteer_activity/volunteer_edit.html', {'form': form})

def volunteer_activity_add(request):
    if request.method == "POST":
        form = UserEventEmployeeForm(request.POST)
        if form.is_valid():
            userevents = form.save(commit=False)
            userevents.save()
            users = User.objects.all()
            userevents = UserEvent.objects.all()
            events = Event.objects.all()
            return render(request, 'volunteer_activity/manage_activity.html',
                          {'volunteer_activity': manage_activity, 'users': users, 'userevents': userevents,
                           'events': events, })
    else:
        form = UserEventEmployeeForm()
        # print("Else")
    return render(request, 'volunteer_activity/volunteer_activity_add.html', {'form': form})

def volunteer_activity_edit(request, pk):
    userevents= get_object_or_404(UserEvent, pk=pk)
    if request.method == "POST":
        # update
        form = UserEventForm(request.POST, instance=userevents)

        if form.is_valid():
            userevents = form.save(commit=False)
            #userevents.updated_date = timezone.now()
            userevents.save()
            #userevents = UserEvent.objects.filter(created_date__lte=timezone.now())
            #userevents = UserEvent.objects.filter(user_num=pk)
            users = User.objects.all()
            userevents = UserEvent.objects.all()
            events = Event.objects.all()
            return render(request, 'volunteer_activity/manage_activity.html',
                          {'volunteer_activity': manage_activity, 'users': users, 'userevents': userevents,
                           'events': events, })
    else:
        # edit
        form = UserEventForm(instance=userevents)
    return render(request, 'volunteer_activity/volunteer_activity_edit.html', {'form': form})

def event_activity_add(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            events = form.save(commit=False)
            events.save()
            users = User.objects.all()
            userevents = UserEvent.objects.all()
            events = Event.objects.all()
            return render(request, 'volunteer_activity/manage_activity.html',
                          {'volunteer_activity': manage_activity, 'users': users, 'userevents': userevents,
                           'events': events, })
    else:
        form = EventForm()
        # print("Else")
    return render(request, 'volunteer_activity/volunteer_activity_add.html', {'form': form})

def event_activity_edit(request, pk):
    events= get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        # update
        form = EventForm(request.POST, instance=events)

        if form.is_valid():
            events = form.save(commit=False)
            #userevents.updated_date = timezone.now()
            events.save()
            #userevents = UserEvent.objects.filter(created_date__lte=timezone.now())
            #userevents = UserEvent.objects.filter(user_num=pk)
            users = User.objects.all()
            userevents = UserEvent.objects.all()
            events = Event.objects.all()
            return render(request, 'volunteer_activity/manage_activity.html',
                          {'volunteer_activity': manage_activity, 'users': users, 'userevents': userevents,
                           'events': events, })
    else:
        # edit
        form = EventForm(instance=events)
    return render(request, 'volunteer_activity/volunteer_activity_edit.html', {'form': form})

######################################################################

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)
            return render(request,
                          'volunteer_activity/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'volunteer_activity/register.html', {'user_form': user_form})

def contactus(request):
   return render(request, 'volunteer_activity/contactus.html',
                 {'volunteer_activity': contactus})

########### My Activity Page ##################
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
#########################

def pwd_recover(request):
   return render(request, 'volunteer_activity/pwd_recover.html',
                 {'volunteer_activity': pwd_recover})


@login_required
def signup(request):
    if request.method == "POST":
        form = UserEventEmployeeForm(request.POST)

        if form.is_valid():
            userevents = form.save(commit=False)
            userevents.save()
            users = User.objects.all()
            userevents = UserEvent.objects.all()
            events = Event.objects.all()
            return render(request, 'volunteer_activity/signup_message.html',
                          {'users': users, 'userevents': userevents,
                           'events': events, })
    else:
        form = UserEventEmployeeForm()
        # print("Else")
    return render(request, 'volunteer_activity/signup.html', {'form': form})