'''importing django forms'''
from django import forms 
# creating a form 
class InputForm(forms.Form):
    '''forms'''
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    email = forms.EmailField(max_length = 200)
    password = forms.CharField(widget = forms.PasswordInput(),
                               help_text = "8 Digits at least")
