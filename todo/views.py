'''importing shortcuts'''
from django.shortcuts import render, redirect
from.models import Todo
# Creating views here.

def homepage(request):
    '''returns the homepage'''
    return render (request,'home.html', {'todos': Todo.objects.all()})
          
def createpage(request):
    '''user can create todo on this page'''
    if request.method=='POST':
        title=request.POST.get('title')
        desc=request.POST.get('description')
        user=request.user
        todo=Todo(user=user,title=title,description=desc)
        todo.save()
        return redirect('home')
    return render(request,'create.html')
          
def submit(request):
    '''Submit button on create page'''
    return render(request,'home.html')
 

