'''importing appconfig'''
from django.apps import AppConfig

class TodoConfig(AppConfig):
    '''Todo config'''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'
