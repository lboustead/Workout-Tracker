# Generated by Django 5.0.6 on 2024-07-01 04:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0011_alter_info_activity_level_alter_info_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeightGoalPounds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_goal', models.CharField(max_length=10)),
                ('pounds_per_week', models.DecimalField(decimal_places=1, max_digits=4)),
            ],
        ),
        migrations.AlterField(
            model_name='info',
            name='weight_goal_pounds',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account_app.weightgoalpounds'),
        ),
    ]
