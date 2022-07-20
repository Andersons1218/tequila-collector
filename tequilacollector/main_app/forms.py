from django.forms import ModelForm
from .models import Taste

class TasteForm(ModelForm):
  class Meta:
    model = Taste
    fields = ['date', 'rims']