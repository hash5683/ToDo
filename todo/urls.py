'''imprting path and views'''
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('create/', views.createpage, name='create'),
    path('edit/<int:todo_id>/', views.edit, name='edit'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('mark_as_done/<int:todo_id>/', views.mark_as_done, name='mark_as_done'),
    path('done/', views.done, name='done'),
]   
