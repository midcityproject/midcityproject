
from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
#from .forms import *
from django.db.models import Sum


def home(request):
   return render(request, 'volunteer_activity/home.html',
                 {'volunteer_activity': home})
