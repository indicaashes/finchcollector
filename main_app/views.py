from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
from .forms import GrubbingForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', 
    { 
        'finches': finches 
    }
)

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  grubbing_form = GrubbingForm()
  return render(request, 'finches/detail.html', { 
     'finch': finch, 'grubbing_form': grubbing_form 
     })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

    success_url = '/finches/{finch_id}'

class FinchUpdate(UpdateView):
  model = Finch

  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'

def add_grubbing(request, finch_id):
    form = GrubbingForm(request.POST)

    if form.is_valid():
    
        new_grubbing = form.save(commit=False)
        new_grubbing.finch_id = finch_id
        new_grubbing.save()
    return redirect('detail', finch_id=finch_id)