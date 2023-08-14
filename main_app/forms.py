from django.forms import ModelForm
from .models import Grubbing

class GrubbingForm(ModelForm):
  class Meta:
    model = Grubbing
    fields = ['date', 'meal']