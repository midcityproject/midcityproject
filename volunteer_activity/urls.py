from django.conf.urls import url
#from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
   # url(r'^login/$', auth_views.login, name='login'),
   # url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    #url(r'^home/$', views.home, name='home'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^contactus/$', views.contactus, name='contactus'),
    url(r'^events/$', views.IndexView.as_view(), name='events'),
    url(r'^events/(?P<pk>\d+)/$', views.DetailView.as_view(), name='event_details'),
    url(r'^tracking/$', views.tracking, name='tracking'),
    url(r'^tracking/(?P<pk>\d+)/edit/$', views.tracking_edit, name='tracking_edit'),
    url(r'^manage_activity/$', views.manage_activity, name='manage_activity'),
   # url(r'^manage_activity_volunteer_activity_edit/(?P<pk>\d+)/edit/$', views.manage_activity_volunteer_activity_edit, name='manage_activity_volunteer_activity_edit'),
    #url(r'^manage_activity_volunteer_edit/(?P<pk>\d+)/edit/$', views.manage_activity_volunteer_edit, name='manage_activity_volunteer_edit'),

    url(r'^signup/$', views.signup, name='signup'),
    url(r'^add_event/$', views.add_event, name='add_event'),
    url(r'^edit_event/$', views.edit_event, name='edit_event'),
    url(r'^pwd_recover/$', views.pwd_recover, name='pwd_recover'),

    ]
