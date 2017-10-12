from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^events/$', views.events, name='events'),
    url(r'^tracking/$', views.tracking, name='tracking'),
    url(r'^contactus/$', views.contactus, name='contactus'),

]
urlpatterns = format_suffix_patterns(urlpatterns)
