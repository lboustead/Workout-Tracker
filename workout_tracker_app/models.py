from datetime import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Workout(models.Model):
    workout_id = models.AutoField(primary_key=True)
    workout_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, db_column="user", on_delete=models.CASCADE, default=0)
    calories_burned = models.IntegerField(default=0)
    date = models.DateField()
    start_time = models.DateTimeField(default=timezone.now)       # Time workout was created
    last_active_time = models.DateTimeField(null=True, blank=True)  # Timestamp of last resume
    active_seconds = models.IntegerField(default=0)  # Accumulated time in seconds
    is_completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.workout_name:
            self.workout_name = self.workout_name.title()
        super().save(*args, **kwargs)

    def get_elapsed_time(self):
        elapsed = self.active_seconds
        if self.last_active_time and not self.is_completed:
            elapsed += int((timezone.now() - self.last_active_time).total_seconds())
        return elapsed
    
    def status(self):
        if self.is_completed:
            return "completed"
        elif self.last_active_time:
            return "active"
        else:
            return "paused"
        
    class Meta:
        verbose_name = "Workout"
        verbose_name_plural = "Workouts"

class Exercise(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.exercise_name:
            self.exercise_name = self.exercise_name.title()
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Exercise"
        verbose_name_plural = "Exercises"
    
class Sets(models.Model):
    set_id = models.AutoField(primary_key=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    set = models.IntegerField()
    reps = models.IntegerField()
    weight = models.FloatField()
    
    class Meta:
        verbose_name = "Set"
        verbose_name_plural = "Sets"

