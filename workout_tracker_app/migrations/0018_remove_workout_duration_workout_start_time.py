# Generated by Django 5.0.6 on 2025-04-12 04:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker_app', '0017_alter_exercise_options_alter_sets_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='duration',
        ),
        migrations.AddField(
            model_name='workout',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
