from django.shortcuts import render, redirect
from pendencia_nacional.models import Março
from pendencia_nacional.forms import MarçoForm


def pendencia(request):
    data = {}
    # data['db'] = Março.objects.all()
    all = Março.objects.all()
    return render(request, 'index.html', data)
