from django.http import HttpResponseRedirect
from django.shortcuts import render
from todoapp.models import ToDoListItem

# Create your views here.


def toDoAppView(request):
    all_to_do_items = ToDoListItem.objects.all()

    return render(request, "index.html", {"allItems": all_to_do_items})

def addTodoView(request):
    x = request.POST['content']
    print(x)
    new_item = ToDoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def clearTodoItemView(request):

    return HttpResponseRedirect('/todoapp/')
