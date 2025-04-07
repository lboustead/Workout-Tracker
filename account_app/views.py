from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import *
from workout_tracker_app.models import Workout
from .models import Info
from .forms import InfoForm


def dashboard(request):
    if request.user.is_authenticated:
        recent_workouts = Workout.objects.filter(user=request.user).order_by('-date')[:10]
        return render(request, 'account_app/dashboard.html', {'recent_workouts': recent_workouts})
    else:
        return redirect('login')

def login_user(request):
    attempts_count=0
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect("dashboard")
        else:
            messages.success(request, "This username or password is incorrect.")
            attempts_count+=1
            return redirect("login")
    else:
        return render(request, "account_app/login.html", {})
    
def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out")
    return redirect('login')

def create_user(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "Registration successfull")
            return redirect('dashboard')
        else:
            messages.error(request, "Username already exists or password did not meet requirements.")
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request, "account_app/create_account.html", {
        'form':form,
        })
    
from django.shortcuts import render, get_object_or_404, redirect
from .models import Info
from .forms import InfoForm

def my_info(request):
    try:
        # Try to fetch the existing Info object for the user
        info = Info.objects.get(user=request.user)
    except Info.DoesNotExist:
        # If it doesn't exist, create a new one
        info = Info(user=request.user)

    if request.method == 'POST':
        form = InfoForm(request.POST, instance=info)
        
        if form.is_valid():
            # Set completion status and determine redirect
            if info.has_completed:
                direction = 'dashboard'
            else:
                direction = 'nutrition_home'
            info.has_completed = True
            info = form.save(commit=False)
            info.save()
            
            return redirect(direction)
    else:
        form = InfoForm(instance=info)

    return render(request, 'account_app/my_info.html', {'form': form})
