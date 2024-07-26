'''importing shortcuts and authentifications '''
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm 
def loginview(request):
    '''login'''
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a success page
            else:
                context['error'] = "Invalid username or password"
    else:
        form = LoginForm()
    context['form'] = form
    return render(request, "login.html", context)

def logoutview(request):
    '''logout'''
    logout(request)
    return redirect('login')  # Redirect to login page after logout

