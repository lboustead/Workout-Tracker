# Generated by Django 5.0.6 on 2024-07-01 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0008_info_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='weight_goal_pounds',
            field=models.DecimalField(choices=[(0.5, '0.5 pounds per week'), (1, '1 pound per week'), (1.5, '1.5 pounds per week'), (2, '2 pounds per week'), (0, '0 pounds per week (maintain)')], decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='info',
            name='activity_level',
            field=models.CharField(choices=[('1', 'Little to no activity'), ('2', 'Exercise 1-3 days a week'), ('3', 'Active 3-5 days a week'), ('4', 'Exercise 6-7 days a week')], default='Lightly Active', max_length=1),
        ),
        migrations.AlterField(
            model_name='info',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='info',
            name='weight_goal',
            field=models.CharField(choices=[('lose', 'Lose'), ('maintain', 'Maintain'), ('gain', 'Gain')], default='maintain', max_length=8),
        ),
    ]