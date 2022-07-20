from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.http import HttpResponse
from .models import Tequila
from .forms import TasteForm


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
    taste_form = TasteForm()
    return render(request, 'tequila/details.html', {'tequila': tequila, 'taste_form': taste_form})

def add_taste(request, tequila_id):
    
  form = TasteForm(request.POST) 
  if form.is_valid():
    new_taste = form.save(commit=False)
    new_taste.tequila_id = tequila_id
    new_taste.save()         
  return redirect('detail', tequila_id=tequila_id)

class TequilaCreate(CreateView):
  model = Tequila
  fields = '__all__'
  success_url = '/tequila/'

class TequilaUpdate(UpdateView):
  model = Tequila
  fields = ['type', 'description' ]
  

class TequilaDelete(DeleteView):
  model = Tequila
  success_url = '/tequila/'

class Meta:
  orerding = ['-date']

