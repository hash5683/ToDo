'''importing the shortcuts and form'''
from django.shortcuts import render
from .forms import InputForm
 
# Create your views here.
def signupview(request):
    '''signup'''
    context ={}
    context['form']= InputForm()
    return render(request, "signup.html", context)
