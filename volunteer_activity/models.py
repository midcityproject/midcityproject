from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#class User(models.Model):
 #   name = models.CharField(max_length=50)
  #  address = models.CharField(max_length=200)
    #user_number = models.IntegerField(blank=False, null=False, primary_key=True)
    #city = models.CharField(max_length=50)
    #state = models.CharField(max_length=50)
    #zipcode = models.CharField(max_length=10)
    #email = models.EmailField(max_length=200)
    #cell_phone = models.CharField(max_length=50)
    #event_name = models.CharField(max_length=200)
    #hours_volunteered = models.CharField(max_length=10)
    #active_inactive = models.CharField(max_length=10)
    #user_type = models.CharField(max_length=10, default = "volunteer")
    #created_date = models.DateTimeField(default=timezone.now)
    #updated_date = models.DateTimeField(auto_now_add=True)


   # def created(self):
      #  self.created_date = timezone.now()
     #   self.save()

    #def updated(self):
    #    self.updated_date = timezone.now()
   #     self.save()

  #  def __str__(self):
 #       return str(self.user_number)


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
