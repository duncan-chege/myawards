from django import forms
from djang.contrib.auth.models import User
from djang.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:     #gives us a nested name space for configs and keeps them in 1 place
        model = User
        fields = ['username','email','password1','password2']
