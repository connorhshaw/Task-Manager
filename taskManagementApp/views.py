from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import TaskDb
from .forms import TaskForm
from django.contrib import messages

def home(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = TaskDb.objects.all()
            messages.success(request, ("New item added"))
            return HttpResponseRedirect(reverse('home'))
        
    else:
        all_items = TaskDb.objects.all()
        return render(request, 'index.html', {'all_items':all_items})

def delete(request, list_id):

    item = TaskDb.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item deleted'))
    return redirect('home')