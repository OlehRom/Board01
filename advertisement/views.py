import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Task, Comment
from .forms import TaskForm
from django.http import Http404, HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.db.models import Q
from django.urls import reverse



def home(request):
    tasks = Task.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'advertisement/home.html', {'tasks':tasks})

def detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    comments_list = task.comment_set.order_by('-id')[:10]
    return render(request, 'advertisement/detail.html', {'task':task, 'comments_list':comments_list})

def leave_comment(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect(reverse('detail', args = (task.id,)))

def new(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.published_date = timezone.now()
            task.save()
            return redirect('detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'advertisement/edit.html', {'form':form})

def edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.published_date = timezone.now()
            task.save()
            return redirect('detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'advertisement/edit.html', {'form': form})

def delete(request, pk):
    try:
        el = Task.objects.get(pk=pk)
        el.delete()
        return HttpResponseRedirect("/")
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Оголошення не знайдено</h2>")

def posts_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        tasks = Task.objects.filter(Q(title__icontains=search_query) | Q(text__icontains=search_query))
    else:
        tasks = Task.objects.all()
    return render(request, 'advertisement/posts_list.html', {'tasks': tasks})

