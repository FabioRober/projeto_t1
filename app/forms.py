from django.forms import ModelForm
from app.models import Cadastro


class CadastroForm(ModelForm):
    class Meta:
        model = Cadastro
        fields = ['gerencia', 'mcu', 'sro', 'unidade', 'vinculacao', 'email']
