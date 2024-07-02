from django.utils import timezone
from nutrition_tracker_app.forms import MealEntryForm, FoodForm
from .models import Meal, Food, MealEntry
from workout_tracker_app.models import Workout
from account_app.models import Info
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import *
from datetime import datetime, timedelta
from django.contrib import messages

def home(request, date=None):
    user_info = Info.objects.get(user=request.user)
    
    if user_info.has_completed:
        today = timezone.localtime().date()
        if date is None:
            date = today
        else:
            date = datetime.strptime(date, '%Y-%m-%d').date()
        # Adjust date based on navigation buttons
        if 'prev' in request.GET:
            date -= timedelta(days=1)
            return redirect('nutrition_home_date', date=date.strftime('%Y-%m-%d'))
        elif 'next' in request.GET:
            date += timedelta(days=1)
            return redirect('nutrition_home_date', date=date.strftime('%Y-%m-%d'))

        # Filter MealEntry objects for the current user and the selected date
        user_workout = Workout.objects.get(user=request.user, date=date)
        logged_foods = MealEntry.objects.filter(user=request.user, date=date)
    
        # Calculate totals based on the filtered entries
    
        total_calories = sum(entry.food.calories*entry.servings for entry in logged_foods)
        total_protein = sum(entry.food.protein*entry.servings for entry in logged_foods)
        total_fat = sum(entry.food.fat*entry.servings for entry in logged_foods)
        total_carb = sum(entry.food.carbs*entry.servings for entry in logged_foods)
        remaining_calories = user_info.calorie_intake-total_calories+user_workout.calories_burned

        title_calculations = [
            {'value': user_info.calorie_intake, 'label': 'Goal', 'operator': '-'},
            {'value': total_calories, 'label': 'Food', 'operator': '+'},
            {'value': user_workout.calories_burned, 'label': 'Exercise', 'operator': '='},
            {'value': remaining_calories, 'label': 'Remaining'}
        ]

        context = {
        'logged_foods': logged_foods,
        'selected_date': date,
        'meals': Meal.choices,
        'total_calories': total_calories,
        'total_protein': total_protein,
        'total_fat': total_fat,
        'total_carb': total_carb,
        'title_calculations': title_calculations
        }
        return render(request, 'nutrition_tracker_app/home.html', context)
    else:
        messages.success(request, "Complete your profile before using nutrition.")
        return redirect('my_info')


def add_meal_entry(request, meal, date):
    if request.method == 'POST':
        form = MealEntryForm(request.POST)
        if form.is_valid():
            food = form.cleaned_data['food']
            servings = form.cleaned_data['servings']

            existing_entry = MealEntry.objects.filter(user=request.user, meal=meal, food=food, date=date).first()
            if existing_entry:
                existing_entry.servings += servings
                existing_entry.save()
            else:
                MealEntry.objects.create(
                    user=request.user,
                    meal=meal,
                    food=food,
                    servings=servings,
                    date=date
                )
            messages.success(request, "Entry Created")
            return redirect('nutrition_home_date', date=date)
    else:
        form = MealEntryForm()

    foods = Food.objects.all()
    current_url = request.build_absolute_uri()
    context = {
        'form': form,
        'meal': meal,
        'foods': foods,
        'date': date,
        'current_url': current_url,
    }
    return render(request, 'nutrition_tracker_app/add_meal_entry.html', context)
    

def add_food(request, meal, date):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Food Added")
            return redirect('add_meal_entry', meal=meal, date=date)
    else:
        form = FoodForm()
    return render(request, 'nutrition_tracker_app/add_food.html', {'form': form})

def delete_entry(request, pk):
    record = MealEntry.objects.get(pk=pk)
    record.delete()
    messages.success(request, "Entry Deleted")
    return redirect('nutrition_home')