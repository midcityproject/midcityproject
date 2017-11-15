from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^contactus/$', views.contactus, name='contactus'),
    url(r'^events/$', views.IndexView.as_view(), name='events'),
    url(r'^events/(?P<pk>\d+)/$', views.DetailView.as_view(), name='event_details'),
    url(r'^tracking/$', views.tracking, name='tracking'),
    url(r'^tracking/(?P<pk>\d+)/edit/$', views.tracking_edit, name='tracking_edit'),
    url(r'^manage_activity/$', views.manage_activity, name='manage_activity'),
    url(r'^manage_activity/(?P<pk>\d+)/edit/$', views.volunteer_activity_edit, name='volunteer_activity_edit'),
    url(r'^manage_activity/create/$', views.volunteer_activity_add, name='volunteer_activity_add'),
    url(r'^manage_activity/(?P<pk>\d+)/edit_volunteer/$', views.volunteer_edit, name='volunteer_edit'),
    url(r'^manage_activity/create_volunteer/$', views.volunteer_add, name='volunteer_add'),
    url(r'^manage_activity/(?P<pk>\d+)/edit_event/$', views.event_activity_edit, name='event_activity_edit'),
    url(r'^manage_activity/create_event/$', views.event_activity_add, name='event_activity_add'),
    url(r'^signup/(?P<pk>\d+)$', views.signup, name='signup'),
    url(r'^pwd_recover/$', views.pwd_recover, name='pwd_recover'),
    # url(r'^events/signup/(?P<pk>\d+)/$', views.signup, name='signup'),

    ]
