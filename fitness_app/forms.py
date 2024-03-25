from django import forms
from .models import Workout, Exercise, Sets
    
class AddWorkoutForm(forms.ModelForm):
    #username = forms.CharField()
    workout_name = forms.CharField(required=True, label="", widget=forms.widgets.TextInput(
        attrs={"class": "form-control", "placeholder": "Workout Name"}))
    date = forms.DateField(required=True, label="", widget=forms.widgets.DateInput(
        attrs={"class": "form-control", "placeholder": "yyyy-mm-dd"}))
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
    weight = forms.FloatField(required=True, label="", widget=forms.widgets.TextInput(
        attrs={"class": "form-control", "placeholder": "weight"}))
    reps = forms.IntegerField(required=True, label="", widget=forms.widgets.TextInput(
        attrs={"class": "form-control", "placeholder": "reps"}))
    class Meta:
        model = Sets
        exclude = ('exercise', 'set')
        fields =[
            "weight",
            "reps"
        ]
        
