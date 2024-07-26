'''imprting path and views'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signupview, name='signup'),
    # Add other paths as needed
]
