'''imprting path and views'''
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createpage, name='create'),
    path('home/', views.homepage, name='home'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('edit/<int:todo_id>/', views.edit, name='edit'),
    path('mark_as_done/<int:todo_id>/', views.mark_as_done, name='mark_done'),
]   
