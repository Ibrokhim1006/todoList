from django.shortcuts import render,redirect

from .models import Todo

def todo_list(request):
    if request.method == 'POST':
        todo = Todo(text=request.POST.get('text'))
        todo.save()
    too = Todo.objects.all()
    return render(request,'myapp/index.html',{'todoo': too})

def delet_doto(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todo_list')
