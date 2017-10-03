from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^$', views.aboutus, name='aboutus'),
    url(r'^$', views.contactus, name='contactus'),
    


]
urlpatterns = format_suffix_patterns(urlpatterns)