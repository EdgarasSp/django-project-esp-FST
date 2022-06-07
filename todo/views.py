from django.shortcuts import render

# Create your views here.


def get_todo_list(request):
#    return HttpResponse("Hello!")  esp use this if just want to return some text for testing
    return render(request, 'todo/todo_list.html')

