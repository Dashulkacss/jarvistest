from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm


# Create your views here.


def index(request):
    # tasks = Task.objects.all()
    # tasks = Task.objects.order_by('-id')[:1]
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': "Main page", 'tasks': tasks})


def about(request):
    return render(request, 'main/contacts.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена некорректно'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
