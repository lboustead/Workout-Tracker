from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', include('account_app.urls')),
    path('admin/', admin.site.urls),
    path('workout_tracker/', include('workout_tracker_app.urls')),
    path('account/', include('account_app.urls')),
    path('nutrition_tracker/', include('nutrition_tracker_app.urls')),

]
