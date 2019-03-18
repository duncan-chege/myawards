from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import Project
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def feed(request):
    projects = Project.objects.all().order_by('-id')
    print (projects)

    return render(request, 'feed.html',{"projects": projects})

# @login_required
# def profile(request,id):
#     user = User.objects.get(id=id)
#     profiles = Profile.objects.get(id=id)
#     return render(request, 'profile.html',{'profiles':profiles, 'user':user})

def review(request,id):
    projo = Project.objects.get(id=id)
    return render(request, 'review.html',{'projo':projo})





