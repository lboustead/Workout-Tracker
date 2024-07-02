# Generated by Django 5.0.3 on 2024-06-04 02:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker_app', '0011_remove_exercise_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout_tracker_app.workout'),
        ),
        migrations.AlterField(
            model_name='sets',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout_tracker_app.exercise'),
        ),
    ]
