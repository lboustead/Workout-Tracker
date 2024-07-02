# Generated by Django 5.0.2 on 2024-03-13 23:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('exercise_id', models.AutoField(primary_key=True, serialize=False)),
                ('exercise_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('memeber_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('date_joined', models.DateField()),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('workout_id', models.AutoField(primary_key=True, serialize=False)),
                ('workout_name', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sets',
            fields=[
                ('set_id', models.AutoField(primary_key=True, serialize=False)),
                ('set', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('weight', models.FloatField()),
                ('exercise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness_app.exercise')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='workout_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness_app.workout'),
        ),
    ]
