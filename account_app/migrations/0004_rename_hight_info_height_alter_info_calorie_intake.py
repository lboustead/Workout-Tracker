# Generated by Django 5.0.3 on 2024-06-23 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0003_alter_info_calorie_intake'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='hight',
            new_name='height',
        ),
        migrations.AlterField(
            model_name='info',
            name='calorie_intake',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]