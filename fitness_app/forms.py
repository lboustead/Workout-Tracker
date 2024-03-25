from django import forms
from .models import Workout, Exercise, Sets
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

class AddWorkoutForm(forms.ModelForm):
    
    workout_name = forms.CharField(required=True, label="", widget=forms.widgets.TextInput(
        attrs={"class": "form-control", "placeholder": "Workout Name"}))
    username = forms.IntegerField
    date = forms.DateField(required=True, label="",widget=forms.widgets.TextInput(
        attrs={"class": "form-control", "placeholder": "Date yyyy-mm-dd"}))
    class Meta:
        model = Workout
        exclude = ('username',)
    
class AddExerciseForm(forms.ModelForm):
    workout = forms.IntegerField
    exercise_name = forms.CharField(required=True, label="", widget=forms.widgets.TextInput(
        attrs={"class": "form-control", "placeholder": "Exercise"}))
    class Meta:
        model = Exercise
        exclude = ('workout',)
        

class AddSetForm(forms.ModelForm):
    exercise = forms.IntegerField
    set = forms.IntegerField
    reps = forms.IntegerField(required=True, label="", widget=forms.widgets.TextInput(
        attrs={"class": "form-control", "placeholder": "reps"}))
    weight = forms.IntegerField(required=True, label="", widget=forms.widgets.TextInput(
        attrs={"class": "form-control", "placeholder": "weight"}))
    class Meta:
        model = Sets
        exclude = ('exercise', 'set')
