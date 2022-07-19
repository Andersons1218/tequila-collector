from django.shortcuts import render
# Create your views here.
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.http import HttpResponse
from .models import Tequila

# Define the home view
def home(request):
  return HttpResponse('<h1>Tequila Me Loco</h1>')

def about(request):
  return render(request, 'about.html')

def tequila_index(request):
    tequilas = Tequila.objects.all()
    return render(request, 'tequila/index.html', {'tequila': tequilas})

def tequila_detail(request, tequila_id):
    tequila = Tequila.objects.get(id=tequila_id)
    return render(request, 'tequila/details.html', {'tequila': tequila})

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