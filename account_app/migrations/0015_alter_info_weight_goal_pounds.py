# Generated by Django 5.0.6 on 2024-07-01 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0014_alter_info_weight_goal_pounds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='weight_goal_pounds',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
    ]
