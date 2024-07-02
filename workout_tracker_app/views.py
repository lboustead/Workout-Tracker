from django.shortcuts import render
from django.urls import reverse
from workout_tracker_app.models import Workout, Exercise, Sets
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth.forms import *
from django.db.models import Count, Sum


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        recent_workouts = Workout.objects.filter(username=request.user).order_by('-date')[:10]
        return render(request, 'workout_tracker_app/home.html', {'recent_workouts': recent_workouts})
    else:
        return redirect('login')
    
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
                return HttpResponseRedirect(reverse(add_exercise, args=(form.pk,)))
        return render(request, "workout_tracker_app/add_workout.html", {"form": temp_form})
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
                return HttpResponseRedirect(reverse(add_set, args=(form.pk,)))
        else:
            return render(request, "workout_tracker_app/add_exercise.html", {"form": temp_form, "workout":workout.pk})
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
            else:
                messages.success(request, "Reps must be a whole number")
                return HttpResponseRedirect(reverse(exercise_details, args=(exercise.pk,)))
        else:
            return render(request, "workout_tracker_app/add_set.html", {"form": temp_form, "exercise": exercise.pk})
    else:
        messages.success(request, "You must be logged in")
        return redirect("login")
    
def delete_workout(request, pk):
    record = Workout.objects.get(pk=pk)
    record.delete()
    messages.success(request, "Workout deleted")
    return redirect('workout_list')

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
    exercises = Exercise.objects.filter(workout_id=pk).order_by('exercise_id').annotate(
        volume=Sum('sets__weight'),
        set_count=Count('sets')
    )
    for e in exercises:
        total_volume = 0
        total_set_count = 0
        sets = Sets.objects.filter(exercise=e)
        for s in sets:
            total_volume += (s.weight*s.reps)
            total_set_count = sets.count
        e.volume = total_volume
        e.set_count = total_set_count
        
    context = {'exercises': exercises,
               'workout': workout}
    return render(request, "workout_tracker_app/workout_details.html", context=context)

def workout_list(request):
    user = request.user
    workouts = Workout.objects.filter(username=user).annotate(
        exercise_count=Count('exercise', distinct=True),
        total_set_count=Count('exercise__sets__set'),
    ).order_by('-date')
    return render(request, 'workout_tracker_app/workout_list.html', {'workouts': workouts})

def exercise_list(request):
    exercises = Exercise.objects.filter(workout__username=request.user)
    return render(request, 'workout_tracker_app/exercise_list.html', {'exercises': exercises})

def exercise_details(request, exercise_pk):
    exercise = Exercise.objects.get(pk=exercise_pk)
    workout = Workout.objects.get(workout_id=exercise.workout.pk)
    sets = Sets.objects.filter(exercise_id=exercise_pk).order_by('-set')
    context = {'sets': sets,
               'exercise': exercise,
               'workout': workout}
    return render(request, "workout_tracker_app/exercise_details.html", context=context)
