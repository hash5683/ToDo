'''importing shortcuts '''
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Todo
from .forms import TodoForm

def homepage(request):
    '''Returns the homepage.'''
    query = request.GET.get('q', '')
    todos = Todo.objects.filter(user=request.user).filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'home.html', {'todos': todos, 'query': query})
    
@login_required(login_url='login')
def createpage(request):
    '''Returns the create todo page.'''
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('home')
    else:
        form = TodoForm()
    return render(request, 'create.html', {'form': form})

@login_required(login_url='login')
def mark_as_done(request, todo_id):
    '''Marks a todo as done.'''
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.is_done = True
    todo.save()
    return redirect('home')

@login_required(login_url='login')
def edit(request, todo_id):
    '''Edits a todo.'''
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'edit.html', {'form': form})

@login_required(login_url='login')
def delete(request, todo_id):
    '''Deletes a todo.'''
    todo = Todo.objects.get(id=todo_id, user=request.user)
    if request.method == "POST":
        todo.delete()
        return redirect('home')
    return render(request, 'delete.html', {'todo': todo})

@login_required(login_url='login')
def done(request):
    '''Shows done todos.'''
    done_todos = Todo.objects.filter(user=request.user, is_done=True)
    return render(request, 'done.html', {'todos': done_todos})
