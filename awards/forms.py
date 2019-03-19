from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Project


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:     #gives us a nested name space for configs and keeps them in 1 place
        model = User
        fields = ['username','email','password1','password2']

class ProjectPostForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','image_path','website_link']