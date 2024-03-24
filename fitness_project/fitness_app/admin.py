from django.contrib import admin
from fitness_app.models import Workout, Exercise, Sets
# Register your models here.
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Sets)