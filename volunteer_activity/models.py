from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
# from django.core.urlresolvers import reverse


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    cell_phone = models.CharField(max_length=50)
    active_inactive = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Event(models.Model):
    event_num = models.IntegerField(blank=False, null=False, primary_key=True)
    #event_num = models.ManyToManyField(event_num, through='UserEvent')
    organization = models.CharField(max_length=200)
    type= models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    short_description = models.CharField(max_length=50)
    number_volunteers = models.CharField(max_length=10)
    status = models.CharField(max_length=50)
    start_date = models.DateField(default=timezone.now)
    #end_date = models.DateField(default=timezone.now, blank=True, null=True)
    time = models.CharField(max_length=10)

    def created(self):
        self.start_date = timezone.now()
        self.save()



    def updated(self):
        self.end_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.event_num)


class UserEvent(models.Model):
    user_num = models.ForeignKey(User)
    event_num = models.ForeignKey(Event)
    hours = models.CharField(max_length=10)

    def created(self):
        self.save()

    def updated(self):
        self.save()

    def __str__(self):
        return str(self.user_num)
