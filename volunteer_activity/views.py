from django.utils import timezone
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Sum
from .models import Event
from django.views import generic
import csv
from django.http import HttpResponse



class IndexView(generic.ListView):
    template_name = 'volunteer_activity/events.html'
    model = Event

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Event.objects.filter(organization__icontains=query)
        else:
            return Event.objects.all().order_by('-start_date')

#     def get_quereyset(self):
#         return Event.objects.all()

class DetailView(generic.DetailView):
    model = Event
    template_name = 'volunteer_activity/event_details.html'

    def get_queryset(self):
        return Event.objects.all()

# class SignupView(generic.DetailView):
#     model=UserEvent
#     template_name = 'volunteer_activity/signup.html'

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
    users = User.objects.all().order_by('username')
    userevents = UserEvent.objects.all().order_by('-user_num')
    events = Event.objects.all().order_by('-start_date')
    return render(request, 'volunteer_activity/manage_activity.html',
                 {'volunteer_activity': manage_activity, 'users': users,'userevents': userevents, 'events': events,})

def volunteer_add(request):
    if request.method == "POST":
        form = UserEmployeeForm(request.POST)
        if form.is_valid():
            users = form.save(commit=False)
            users.save()
            users = User.objects.all().order_by('username')
            userevents = UserEvent.objects.all().order_by('-user_num')
            events = Event.objects.all().order_by('-start_date')
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
            users = User.objects.all().order_by('username')
            userevents = UserEvent.objects.all().order_by('-user_num')
            events = Event.objects.all().order_by('-start_date')
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
            users = User.objects.all().order_by('username')
            userevents = UserEvent.objects.all().order_by('-user_num')
            events = Event.objects.all().order_by('-start_date')
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
        form = UserEventEmployeeForm(request.POST, instance=userevents)

        if form.is_valid():
            userevents = form.save(commit=False)
            #userevents.updated_date = timezone.now()
            userevents.save()
            #userevents = UserEvent.objects.filter(created_date__lte=timezone.now())
            #userevents = UserEvent.objects.filter(user_num=pk)
            users = User.objects.all().order_by('username')
            userevents = UserEvent.objects.all().order_by('-user_num')
            events = Event.objects.all().order_by('-start_date')
            return render(request, 'volunteer_activity/manage_activity.html',
                          {'volunteer_activity': manage_activity, 'users': users, 'userevents': userevents,
                           'events': events, })
    else:
        # edit
        form = UserEventEmployeeForm(instance=userevents)
    return render(request, 'volunteer_activity/volunteer_activity_edit.html', {'form': form})

def event_activity_add(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            events = form.save(commit=False)
            events.save()
            users = User.objects.all().order_by('username')
            userevents = UserEvent.objects.all().order_by('-user_num')
            events = Event.objects.all().order_by('-start_date')
            return render(request, 'volunteer_activity/manage_activity.html',
                          {'volunteer_activity': manage_activity, 'users': users, 'userevents': userevents,
                           'events': events, })
    else:
        form = EventForm()
        # print("Else")
    return render(request, 'volunteer_activity/event_activity_add.html', {'form': form})

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
            users = User.objects.all().order_by('username')
            userevents = UserEvent.objects.all().order_by('-user_num')
            events = Event.objects.all().order_by('-start_date')
            return render(request, 'volunteer_activity/manage_activity.html',
                          {'volunteer_activity': manage_activity, 'users': users, 'userevents': userevents,
                           'events': events, })
    else:
        # edit
        form = EventForm(instance=events)
    return render(request, 'volunteer_activity/event_activity_edit.html', {'form': form})

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
def signup(request, pk):
    if request.method == "POST":
        form = UserEventSignupForm(request.POST)
        if form.is_valid():
            userevents = form.save(commit=False)
            userevents.user_num = User.objects.get(username=request.user)
            userevents.event_num = get_object_or_404(Event, pk=pk)
            userevents.hours = 0
            userevents.save()
            #send_mail(subject, message, from_email, to_list, fail_silently=true)
            subject = "Mid-City Gives Back"
            message = "Thank you for signing up for an event"
            from_email = settings.EMAIL_HOST_USER
            to_list = [request.user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            userevents = UserEvent.objects.filter(user_num=request.user.pk).order_by('-event_num')[:5]
            events = Event.objects.all().order_by('-start_date')[:5]
            return render(request, 'volunteer_activity/home.html',
                          {'volunteer_activity': home, 'events': events, 'userevents': userevents, })
    else:
        form = UserEventSignupForm()
        # print("Else")
    return render(request, 'volunteer_activity/signup.html', {'form': form})


def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response

