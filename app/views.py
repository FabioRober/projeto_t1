from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from app.forms import CadastroForm
from app.models import Cadastro



def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Cadastro.objects.filter(unidade__icontains=search)
    else:
        #data['db'] = Cadastro.objects.all()
        all = Cadastro.objects.all()
        paginator = Paginator(all, 8)
        pages = request.GET.get('page')
        data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = CadastroForm()
    return render(request, 'form.html', data)


def create(request):
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):#pk = primary key
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    data['form'] = CadastroForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    form = CadastroForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Cadastro.objects.get(pk=pk)
    db.delete()
    return redirect('home')
