# Generated by Django 5.0.2 on 2025-04-07 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker_app', '0016_exercise_notes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'verbose_name': 'Exercise', 'verbose_name_plural': 'Exercises'},
        ),
        migrations.AlterModelOptions(
            name='sets',
            options={'verbose_name': 'Set', 'verbose_name_plural': 'Sets'},
        ),
        migrations.AlterModelOptions(
            name='workout',
            options={'verbose_name': 'Workout', 'verbose_name_plural': 'Workouts'},
        ),
    ]
