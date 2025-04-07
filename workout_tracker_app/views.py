from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Workout, Exercise, Sets
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.contrib.auth.forms import *
from django.db.models import Count, Sum
from django.utils import timezone


# Create your views here.
def start_workout(request):
    temp_form = AddWorkoutForm(request.POST or None)
    if request.method == "POST":
        if temp_form.is_valid():
            form = temp_form.save(commit=False)
            form.user = request.user
            form.date = timezone.localtime().date()
            form.save()
            messages.success(request, "New Workout Created")
            return HttpResponseRedirect(reverse(workout_details, args=(form.pk,)))
    else:
        return render(request, "workout_tracker_app/start_workout.html", {"form": temp_form})

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

def workout_list(request):
    workouts = Workout.objects.filter(user=request.user).annotate(
    ).order_by('-date')[:10]
    return render(request, 'workout_tracker_app/workout_list.html', {'workouts': workouts})

def workout_details(request, pk):
    # Fetch the current workout
    workout = Workout.objects.get(pk=pk)

    # Fetch all exercises associated with the workout
    exercises = Exercise.objects.filter(workout_id=pk).order_by('exercise_id').annotate(
        volume=Sum('sets__weight'),
        set_count=Count('sets')
    )

    # Handle form submissions
    if request.method == "POST":
        # Handle adding a new exercise
        if "add_exercise" in request.POST:
            temp_form = AddExerciseForm(request.POST)
            if temp_form.is_valid():
                form = temp_form.save(commit=False)
                form.workout = workout
                form.save()
                messages.success(request, f"Exercise '{form.exercise_name}' added successfully.")
                return HttpResponseRedirect(reverse('exercise_details', args=(form.pk,)))
            else:
                messages.error(request, "Error adding exercise. Please check the input values.")

        # Handle saving changes to workout name
        if "save_changes" in request.POST:
            workout_name = request.POST.get("workout_name")
            if workout_name and workout_name != workout.workout_name:
                workout.workout_name = workout_name
                workout.save()
                messages.success(request, "Workout name updated successfully.")
                return HttpResponseRedirect(reverse('workout_details', args=(pk,)))

    temp_form = AddExerciseForm()

    context = {
        'exercises': exercises,
        'workout': workout,
        'form': temp_form,
    }
    return render(request, "workout_tracker_app/workout_details.html", context)


def exercise_details(request, exercise_pk):
    # Fetch the current exercise and related workout
    exercise = Exercise.objects.get(pk=exercise_pk)
    workout = Workout.objects.get(workout_id=exercise.workout.pk)
    sets = Sets.objects.filter(exercise_id=exercise_pk).order_by('set')
    num_sets = Sets.objects.filter(exercise=exercise).count() + 1

    if request.method == "POST":
        # Handle adding a new set
        if "add_set" in request.POST:
            temp_form = AddSetForm(request.POST)
            if temp_form.is_valid():
                form = temp_form.save(commit=False)
                form.exercise = exercise
                form.set = num_sets
                form.save()
                messages.success(request, "New Set Created")
                return HttpResponseRedirect(reverse('exercise_details', args=(exercise_pk,)))
            else:
                messages.error(request, "Error adding set. Please check the input values.")

        # Handle saving changes to existing sets and exercise name
        if "save_changes" in request.POST:
            # Update exercise name
            exercise_name = request.POST.get("exercise_name")
            if exercise_name and exercise_name != exercise.exercise_name:
                exercise.exercise_name = exercise_name
                exercise.save()

            # Update sets
            for s in sets:
                weight = request.POST.get(f"weight_{s.set_id}")
                reps = request.POST.get(f"reps_{s.set_id}")
                try:
                    s.weight = float(weight) if weight else s.weight
                    s.reps = int(reps) if reps else s.reps
                    s.save()
                except ValueError:
                    messages.error(request, f"Invalid input for Set #{s.set}. Please enter valid numbers.")
            messages.success(request, "Changes saved successfully.")
            return HttpResponseRedirect(reverse('exercise_details', args=(exercise_pk,)))

    temp_form = AddSetForm()

    context = {
        'sets': sets,
        'exercise': exercise,
        'workout': workout,
        'forms': temp_form,
    }
    return render(request, "workout_tracker_app/exercise_details.html", context)


from datetime import timedelta

def end_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)

    # Get the timer duration from the form
    timer_duration = request.POST.get("timer_duration")
    if timer_duration:
        workout.duration = timedelta(seconds=int(timer_duration))

    workout.save()
    return redirect('workout_list')