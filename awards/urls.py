from django.conf.urls import url
from . import views
from django.contrib.auth import views

urlpatterns=[
    url('^$',views.LoginView, name='login'),
    url(r'^register',views.register, name='register'),
    url(r'^profile',views.profile, name='profile') 
]