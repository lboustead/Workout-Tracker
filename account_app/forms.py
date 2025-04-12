from django import forms
from .models import Info

# Dropdown choices for goal pounds per week
GOAL_POUNDS_CHOICES = [
    (2.0, "+2.0 lbs/week"),
    (1.5, "+1.5 lbs/week"),
    (1.0, "+1.0 lbs/week"),
    (0.5, "+0.5 lbs/week"),
    (0.0, "Maintain"),
    (-0.5, "-0.5 lbs/week"),
    (-1.0, "-1.0 lbs/week"),
    (-1.5, "-1.5 lbs/week"),
    (-2.0, "-2.0 lbs/week"),
]

class InfoForm(forms.ModelForm):
    height_feet = forms.IntegerField(
        label='Height (feet)', 
        min_value=0, 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    height_inches_remainder = forms.IntegerField(
        label='Height (inches)', 
        min_value=0, 
        max_value=11, 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    weight_goal_pounds = forms.ChoiceField(
        label="Goal Lbs./Week",
        choices=GOAL_POUNDS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Info
        fields = [
            'current_weight',
            'goal_weight',
            'calorie_intake',
            'age',
            'gender',
            'activity_level',
            'weight_goal_pounds',  # Custom field added manually
            'height_feet',
            'height_inches_remainder',
        ]
        widgets = {
            'current_weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'goal_weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'calorie_intake': forms.NumberInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'activity_level': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pre-fill height values from model
        if self.instance and self.instance.height_inches is not None:
            feet = int(self.instance.height_inches) // 12
            inches = int(self.instance.height_inches) % 12
            self.fields['height_feet'].initial = feet
            self.fields['height_inches_remainder'].initial = inches

    def clean(self):
        cleaned_data = super().clean()
        feet = cleaned_data.get('height_feet', 0)
        inches = cleaned_data.get('height_inches_remainder', 0)
        cleaned_data['height_inches'] = feet * 12 + inches
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.height_inches = self.cleaned_data['height_inches']
        if commit:
            instance.save()
        return instance
