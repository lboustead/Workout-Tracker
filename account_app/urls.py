from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('create_account/', views.create_user, name='create_account'),
    path('myinfo/', views.my_info, name='my_info'),
]
