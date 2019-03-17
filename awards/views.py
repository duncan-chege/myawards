from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import Project

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

def review(request,id):
    user=User.objects.get(id=id)
    projects = Project.objects.all().filter(owner_id=user.id)
    return render(request, 'review.html',{'projects':projects,"user":user})




