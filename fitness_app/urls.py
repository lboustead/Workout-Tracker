from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('account/', views.create_user, name='account'),

    path('add_workout/', views.add_workout, name='add_workout'),
    path('add_exercise/<int:pk>/', views.add_exercise, name='add_exercise'),
    path('add_set/<int:pk>/', views.add_set, name='add_set'),

    path('delete_workout/<int:pk>/', views.delete_workout, name='delete_workout'),
    path('delete_exercise/<int:pk>/', views.delete_exercise, name='delete_exercise'),
    path('delete_set/<int:pk>/', views.delete_set, name='delete_set'),
    
    path('my_workouts/', views.workout_list, name='workout_list'),
    path('my_exercises/', views.exercise_list, name='exercise_list'),
    path('workout_details/<int:pk>/', views.workout_details, name='workout_details'),
    path('exercise_details/<int:exercise_pk>/', views.exercise_details, name='exercise_details'),
    
    
]
