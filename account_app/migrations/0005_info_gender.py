# Generated by Django 5.0.3 on 2024-06-24 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0004_rename_hight_info_height_alter_info_calorie_intake'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1),
        ),
    ]
