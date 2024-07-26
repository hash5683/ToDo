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

def delete(request, todo_id):
    '''delete a todo'''
    todo=Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')

def edit(request, todo_id):
    '''edit a todo'''
    todo=Todo.objects.get(id=todo_id)
    if request.method=='POST':
        title=request.POST.get('title')
        desc=request.POST.get('description')
        todo.title=title
        todo.description=desc
        todo.save()
        return redirect('home')
    return render(request,'edit.html', {'todo': todo})

def mark_as_done(request, todo_id):
    '''mark a todo as done'''
    todo=Todo.objects.get(id=todo_id)
    todo.is_done=True
    todo.save()
    return redirect('home')
          
def submit(request):
    '''Submit button on create page'''
    return render(request,'home.html')


 
