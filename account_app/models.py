from django.db import models
from django.contrib.auth.models import User

class Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    has_completed = models.BooleanField(default=False)
    current_weight = models.FloatField()
    goal_weight = models.FloatField()
    calorie_intake = models.IntegerField(blank=True, null=True)
    height = models.FloatField()
    age = models.IntegerField(default=40)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F','Female')), default='M')
    activity_level = models.CharField(max_length=1, choices=(
        ('1', 'Little to no activity'),
        ('2', 'Exercise 1-3 days a week'),
        ('3','Active 3-5 days a week'),
        ('4', 'Exercise 6-7 days a week')
    ), default='1')
    weight_goal = models.CharField(max_length=10, choices=(
        ('lose', 'Lose Weight'),
        ('maintain', 'Maintain Weight'),
        ('gain', 'Gain Weight'),
    ), default='maintain')
    weight_goal_pounds = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)


    def __str__(self):
        return f"Username: {self.user}"
