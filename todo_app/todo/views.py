from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todoItem
# Create your views here.

def todoView(request):
    all = todoItem.objects.all()
    return render(request, "todo.html", {'all':all })

def todoAdd(request):
    new_item =  todoItem ( content = request.POST['content'] )
    new_item.save()
    return redirect('/todo/')

def todoDelete(request , todo_id ):
    new_item = todoItem ( id = todo_id).delete()
    return redirect("/todo/")