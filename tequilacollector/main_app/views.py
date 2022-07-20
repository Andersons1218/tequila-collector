from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.http import HttpResponse
from .models import Tequila, Mix
from .forms import TasteForm
from django.views.generic import ListView, DetailView


# Define the home view
def home(request):
  return render(request,'home.html')

def about(request):
  return render(request, 'about.html')

def tequila_index(request):
    tequilas = Tequila.objects.all()
    return render(request, 'tequila/index.html', {'tequila': tequilas})

def tequila_detail(request, tequila_id):
    tequila = Tequila.objects.get(id=tequila_id)
    id_list = tequila.mixes.all().values_list('id')
    mixes_tequila_doesnt_have = Mix.objects.exclude(id__in=id_list)
    taste_form = TasteForm()
    return render(request, 'tequila/details.html', {'tequila': tequila, 'taste_form': taste_form, 'mixes': mixes_tequila_doesnt_have})

def add_taste(request, tequila_id):
    
  form = TasteForm(request.POST) 
  if form.is_valid():
    new_taste = form.save(commit=False)
    new_taste.tequila_id = tequila_id
    new_taste.save()         
  return redirect('detail', tequila_id=tequila_id)

class TequilaCreate(CreateView):
  model = Tequila
  fields = ['name', 'type', 'description']
  success_url = '/tequila/'

class TequilaUpdate(UpdateView):
  model = Tequila
  fields = ['type', 'description' ]
  

class TequilaDelete(DeleteView):
  model = Tequila
  success_url = '/tequila/'

class Meta:
  orerding = ['-date']

class MixList(ListView):
  model = Mix

class MixDetail(DetailView):
  model = Mix

class MixCreate(CreateView):
  model = Mix
  fields = '__all__'

class MixUpdate(UpdateView):
  model = Mix
  fields = ['name', 'type']

class MixDelete(DeleteView):
  model = Mix
  success_url = '/Mix/'

def assoc_mix(request, tequila_id, mix_id):
  # Note that you can pass a Mix's id instead of the whole Mix object
  Tequila.objects.get(id=tequila_id).mixes.add(mix_id)
  return redirect('detail', tequila_id=tequila_id)

