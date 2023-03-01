from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.Welcome, name = 'Welcome' ),
    path('user', views.User, name = 'User'),
]