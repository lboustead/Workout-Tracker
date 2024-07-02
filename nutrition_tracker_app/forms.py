from django import forms
from .models import Food, MealEntry

class MealEntryForm(forms.ModelForm):
    class Meta:
        model = MealEntry
        fields = ['food', 'servings']
        
class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'calories', 'fat', 'protein', 'carbs', 'serving_size']
