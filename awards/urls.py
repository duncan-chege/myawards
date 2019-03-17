from django.conf.urls import url
from . import views
from django.contrib.auth import views

urlpatterns=[
    url('^$',views.register, name='register'),
    url(r'^login',views.LoginView, name='login'),
    url(r'^logout',views.LogoutView, name='logout')
]