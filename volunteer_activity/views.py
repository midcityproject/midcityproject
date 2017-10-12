from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status





def home(request):
   return render(request, 'volunteer_activity/home.html',
                 {'home': home})

def aboutus(request):
   return render(request, 'volunteer_activity/aboutus.html',
                 {'aboutus': aboutus})

def activity(request):
   return render(request, 'volunteer_activity/events.html',
                 {'events': events})

def tracking(request):
   return render(request, 'volunteer_activity/tracking.html',
                 {'trackingy': tracking})


def contactus(request):
   return render(request, 'volunteer_activity/contactus.html',
                 {'contactus': contactus})





#
