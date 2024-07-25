from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from.models import Todo
# Create your views here.
@login_required(login_url='login')

def homepage(request):
    return render (request,'home.html', {'todos': Todo.objects.all()})

def signuppage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')
           
def createpage(request):
    if request.method=='POST':
        title=request.POST.get('title')
        desc=request.POST.get('description')
        user=request.user
        todo=Todo(user=user,title=title,description=desc)
        todo.save()
        return redirect('home')
    return render(request,'create.html')    
           
def submit(request):
    return render(request,'home.html')   
