from django import forms
from .models import Workout, Exercise, Sets
from django.forms.widgets import NumberInput

class AddWorkoutForm(forms.ModelForm):
    workout_name = forms.CharField(
        required=True, 
        label="", 
        widget=forms.widgets.TextInput(
        attrs={"class": "form-control", "placeholder": "Workout Name"}))
    
    class Meta:
        model = Workout
        exclude = ('user', 'date', 'calories_burned')
        fields = ['workout_name']
    
class AddExerciseForm(forms.ModelForm):
    #workout = forms.IntegerField
    exercise_name = forms.CharField(required=True, label="", widget=forms.widgets.TextInput(
        attrs={"class": "form-control", "placeholder": "Exercise"}))
    class Meta:
        model = Exercise
        exclude = ('workout',)
        fields = ['exercise_name']
        
class AddSetForm(forms.ModelForm):
    weight = forms.FloatField(required=True, label="", widget=forms.widgets.TextInput(
        attrs={"class": "form-control bg-dark text-light border-secondary", "placeholder": "Weight (lbs)"}))
    reps = forms.IntegerField(required=True, label="", widget=forms.widgets.TextInput(
        attrs={"class": "form-control bg-dark text-light border-secondary", "placeholder": "Reps"}))
    class Meta:
        model = Sets
        exclude = ('exercise', 'set')
        fields =["weight", "reps"]