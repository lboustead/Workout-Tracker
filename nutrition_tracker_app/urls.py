from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.home, name='nutrition_home'),
    path('dashboard/<str:date>/', views.home, name='nutrition_home_date'),
    path('add_food/<str:meal>/<str:date>/', views.add_food, name='add_food'),
    path('add_meal_entry/<str:meal>/<str:date>/', views.add_meal_entry, name='add_meal_entry'),
    path('delete_meal_entry/<int:pk>', views.delete_entry, name='delete_entry'),
]