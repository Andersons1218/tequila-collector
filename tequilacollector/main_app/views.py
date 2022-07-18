from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
class Tequila:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, type, description):
    self.name = name
    self.type = type
    self.description = description
    

tequila = [
  Tequila('Casa Migos', 'blanco', 'a light fruit-driven tequila with flavors of papaya, guava, and vanilla'),
  Tequila('Patron', 'resposado', 'A sophisticated silver tequila with a perfectly balanced, very complex smoky flavor'),
  Tequila('Jose Cuervo', 'anejo', 'light gold spirit has a sweet aroma with pleasant agave notes' )
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Tequila Me Loco</h1>')

def about(request):
  return render(request, 'about.html')

def tequila_index(request):
  return render(request, 'tequila/index.html', {'tequila': tequila})

