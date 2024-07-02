from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workout(models.Model):
    workout_id = models.AutoField(primary_key=True)
    workout_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, db_column="user", on_delete=models.CASCADE, default=0)
    calories_burned = models.IntegerField(default=0)
    date = models.DateField()

class Exercise(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=100)
    
class Sets(models.Model):
    set_id = models.AutoField(primary_key=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    set = models.IntegerField()
    reps = models.IntegerField()
    weight = models.FloatField()
