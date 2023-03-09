from django.forms import ModelForm
from pendencia_nacional.models import Março


class MarçoForm(ModelForm):
    class Meta:
        model = Março
        fields = ['data', 'siglase', 'cargalancada', 'cargabaixada', 'percentual',]