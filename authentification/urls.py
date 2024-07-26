'''importing urls'''
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    # Add other paths as needed
]
