'''importing shortcuts'''
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from.models import Todo
# Creating views here.

def homepage(request):
    '''Returns the homepage.'''
    query = request.GET.get('q', '')
    todos = Todo.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'home.html', {'todos': todos, 'query': query})
    
       
@login_required(login_url='login')
def createpage(request):
    '''Returns the create todo page.'''
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = Todo(user=request.user, title=title, description=description)
        todo.save()
        return redirect('home')
    return render(request, 'create.html')

def mark_as_done(todo_id):
    '''Marks a todo as done.'''
    todo = Todo.objects.get(id=todo_id)
    todo.is_done = True
    todo.save()
    return redirect('home')

def edit(request, todo_id):
    '''Returns the edit todo page.'''
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect('home')
    return render(request, 'edit.html', {'todo': todo})

def delete(request, todo_id):
    '''Returns the delete todo page.'''
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        todo.delete()
        return redirect('home')
    return render(request, 'delete.html', {'todo': todo})
