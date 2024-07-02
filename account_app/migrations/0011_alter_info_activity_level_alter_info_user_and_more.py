# Generated by Django 5.0.6 on 2024-07-01 04:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0010_alter_info_weight_goal_alter_info_weight_goal_pounds'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='activity_level',
            field=models.CharField(choices=[('1', 'Little to no activity'), ('2', 'Exercise 1-3 days a week'), ('3', 'Active 3-5 days a week'), ('4', 'Exercise 6-7 days a week')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='info',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='info',
            name='weight_goal_pounds',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
        ),
    ]