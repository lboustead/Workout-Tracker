# Generated by Django 5.0.6 on 2024-12-22 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker_app', '0014_rename_username_workout_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
