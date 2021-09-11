from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from todos.models import Activity


def activity(request, title):
    indTodo = Activity.objects.get(title=title)
    return render(request, 'todos/individual-activity.html',{'inds':indTodo})
