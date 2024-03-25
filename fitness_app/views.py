from django.shortcuts import render
from django.urls import reverse
from fitness_app.models import Workout, Exercise, Sets
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import AddWorkoutForm, AddExerciseForm, AddSetForm
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Count


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        workouts = Workout.objects.filter(username=request.user).annotate(exercise_count=Count('exercise')).order_by('-date')
        
        #getting each exercise in the workout requested
        #Assigning set_count to count number of sets in each workout
        if workouts:
            for w in workouts:
                exercises = Exercise.objects.filter(workout=w).annotate(set_count=Count('sets'))
            
                #calculate totals in workout
                total_set_count = 0
                total_volume = 0
                for e in exercises:
                    sets = Sets.objects.filter(exercise=e)
                    for s in sets:
                        total_volume += (s.weight*s.reps)
                    total_set_count += e.set_count
                w.total_set_count = total_set_count
                w.total_volume = total_volume
        
        #Establishing context
        context = {'workouts': workouts,
                   }
        return render(request, 'fitness_app/home.html', context=context)
    else:
        return redirect('login')




def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been authenticated and successfully logged in.")
            return redirect("home")
        else:
            messages.success(request, "This username or password is incorrect.")
            return redirect("login")
    else:
        return render(request, "fitness_app/login.html", {})
    
def logout_user(request):
    logout(request)
    
    messages.success(request, "You have been successfully logged out")
    return redirect('login')

def create_user(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "Registration successfull")
            return redirect('home')
    else:
        form = UserCreationForm()
        return render(request, "fitness_app/account.html", {
            'form':form,
        })
    
    
def add_workout(request):
    user_name = request.user
    temp_form = AddWorkoutForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if temp_form.is_valid():
                form = temp_form.save(commit=False)
                form.username = user_name
                form.save()
                messages.success(request, "New Workout Created")
                return HttpResponseRedirect(reverse(workout_details, args=(form.pk,)))
        return render(request, "fitness_app/add_workout.html", {"form": temp_form})
    else:
        messages.success(request, "You must be logged in")
        return redirect("login")

def add_exercise(request, pk):
    workout = Workout.objects.get(pk=pk)
    temp_form = AddExerciseForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if temp_form.is_valid():
                form = temp_form.save(commit=False)
                form.workout = workout
                form.save()
                messages.success(request, "New Exercise Created")
                return HttpResponseRedirect(reverse(exercise_details, args=(form.pk,)))
        return render(request, "fitness_app/add_exercise.html", {"form": temp_form})
    else:
        messages.success(request, "You must be logged in")
        return redirect("login")
    
def add_set(request, pk):
    exercise = Exercise.objects.get(pk=pk)
    num_sets = Sets.objects.filter(exercise=exercise).count()+1
    temp_form = AddSetForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if temp_form.is_valid():
                form = temp_form.save(commit=False)
                form.exercise = exercise
                form.set = num_sets
                form.save()
                messages.success(request, "New Set Created")
                return HttpResponseRedirect(reverse(exercise_details, args=(exercise.pk,)))
        return render(request, "fitness_app/add_set.html", {"form": temp_form})
    else:
        messages.success(request, "You must be logged in")
        return redirect("login")
    

    

def delete_workout(request, pk):
    record = Workout.objects.get(pk=pk)
    record.delete()
    messages.success(request, "Workout deleted")
    return redirect('home')

def delete_exercise(request, pk):
    record = Exercise.objects.get(pk=pk)
    workout = Workout.objects.get(workout_id=record.workout.pk)
    record.delete()
    messages.success(request, "Exercise deleted")
    return HttpResponseRedirect(reverse(workout_details, args=(workout.pk,)))

def delete_set(request, pk):
    record = Sets.objects.get(pk=pk)
    exercise = Exercise.objects.get(exercise_id=record.exercise.pk)
    workout = Workout.objects.get(workout_id=exercise.workout.pk)
    record.delete()
    messages.success(request, "Set deleted")
    return HttpResponseRedirect(reverse(exercise_details, args=(exercise.pk,)))




def workout_details(request, pk):
    workout = Workout.objects.get(pk=pk)
    exercises = Exercise.objects.filter(workout_id=pk).order_by('exercise_id')

    context = {'exercises': exercises,
               'workout': workout}
    return render(request, "fitness_app/workout_details.html", context=context)

def exercise_details(request, exercise_pk):
    exercise = Exercise.objects.get(pk=exercise_pk)
    workout = Workout.objects.get(workout_id=exercise.workout.pk)
    sets = Sets.objects.filter(exercise_id=exercise_pk).order_by('set')
    context = {'sets': sets,
               'exercise': exercise,
               'workout': workout}
    return render(request, "fitness_app/exercise_details.html", context=context)
