from django import forms
from .models import Info

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['current_weight', 'goal_weight', 'calorie_intake', 'height', 'age', 'gender', 'activity_level', 'weight_goal', 'weight_goal_pounds']
        widgets = {
            'current_weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'goal_weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'calorie_intake': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'activity_level': forms.Select(attrs={'class': 'form-control'}),
            'weight_goal': forms.Select(attrs={'class': 'form-control'}),
            'weight_goal_pounds': forms.NumberInput(attrs={'class': 'form-control'}),
        }
