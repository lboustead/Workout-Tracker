from django.urls import path, include
from . import views

urlpatterns = [
    path('workout_list/', views.workout_list, name='workout_list'),

    path('start_workout/', views.start_workout, name='start_workout'),
    path('end_workout/<int:workout_id>/', views.end_workout, name='end_workout'),

    path('workout_details/<int:pk>/', views.workout_details, name='workout_details'),
    path('exercise_details/<int:exercise_pk>/', views.exercise_details, name='exercise_details'),
    
    path('delete_workout/<int:pk>/', views.delete_workout, name='delete_workout'),
    path('delete_exercise/<int:pk>/', views.delete_exercise, name='delete_exercise'),
    path('delete_set/<int:pk>/', views.delete_set, name='delete_set'),
    
    path('workout/<int:workout_id>/pause/', views.pause_workout, name='pause_workout'),
    path('workout/<int:workout_id>/resume/', views.resume_workout, name='resume_workout'),

]
