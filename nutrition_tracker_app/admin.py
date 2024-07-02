from django.contrib import admin
from .models import MealEntry, Food

admin.site.register(Food)
admin.site.register(MealEntry)

