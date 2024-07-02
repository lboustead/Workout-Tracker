from django.db import models
from django.contrib.auth.models import User

class Meal(models.TextChoices):
    BREAKFAST = 'breakfast', 'Breakfast'
    LUNCH = 'lunch', 'Lunch'
    DINNER = 'dinner', 'Dinner'
    SNACK = 'snack', 'Snack'

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    fat = models.IntegerField()
    protein = models.IntegerField()
    carbs = models.IntegerField()
    serving_size = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} serving size of {self.serving_size} has {self.calories} Calories"

class MealEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.CharField(max_length=255, choices=Meal.choices)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    servings = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.food.name} - {self.food.protein*self.servings}g protein - {self.food.fat*self.servings}g fat - {self.food.carbs*self.servings}g carbs - {self.servings} Servings - {self.food.calories*self.servings} Calories"

