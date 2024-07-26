'''imprting form'''
from django import forms

class LoginForm(forms.Form):
    '''login form'''
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
    
