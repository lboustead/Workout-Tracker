# Generated by Django 5.0.6 on 2024-07-01 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0013_alter_info_weight_goal_pounds_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='weight_goal_pounds',
            field=models.FloatField(default=0.0),
        ),
    ]
