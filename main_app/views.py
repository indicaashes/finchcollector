from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


from .models import Finch, Plaything
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
    id_list = finch.playthings.all().values_list('id')
    
    playthings_finch_doesnt_have = Plaything.objects.exclude(id__in=id_list)
    grubbing_form = GrubbingForm()
    return render(request, 'finches/detail.html', { 
        'finch': finch, 'grubbing_form': grubbing_form,
        'playthings': playthings_finch_doesnt_have
        })

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'breed', 'description', 'age']

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

class PlaythingList(ListView):
  model = Plaything

class PlaythingDetail(DetailView):
  model = Plaything

class PlaythingCreate(CreateView):
  model = Plaything
  fields = '__all__'

class PlaythingUpdate(UpdateView):
  model = Plaything
  fields = ['name', 'color']

class PlaythingDelete(DeleteView):
  model = Plaything
  success_url = '/playthings'

def assoc_plaything(request, finch_id, plaything_id):
   Finch.objects.get(id=finch_id).playthings.add(plaything_id)
   return redirect('detail', finch_id=finch_id)


def unassoc_plaything(request, finch_id, plaything_id):
     Finch.objects.get(id=finch_id).playthings.remove(plaything_id)
     return redirect('detail', finch_id=finch_id)
