from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
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
def feed(request):
    projects = Project.objects.all().order_by('-id')
    print (projects)

    return render(request, 'feed.html',{"projects": projects})

def review(request,id):
    projo = Project.objects.get(id=id)
    return render(request, 'review.html',{'projo':projo})

def profile(request,id):
    user = User.objects.get(id=id)
    profiles = Profile.objects.all()
    projects = Profile.objects.all().filter(owner_id=user.id)
    return render(request, 'profile.html',{'profiles':profiles, 'user':user})

def post(request):
    user = request.user
    if request.method == 'POST':
        projform = ProjectPostForm(request.POST, request.FILES)
        if projform.is_valid():
            proj = projform.save(commit=False)
            proj.owner = user
            proj.save()
        return redirect('profile', user.id)
    else:
        projform = ProjectPostForm()
    return render(request, 'newproj.html', {'projform': projform})







