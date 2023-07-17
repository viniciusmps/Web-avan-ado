
from django.shortcuts import render
from cadastro_app.models import Cadastro
def index(request):
    cadastro = Cadastro.objects.all()
    testChave = {
    'cadastro': cadastro

    }

    return render(request, 'index.html', testChave)
def cadastro(request, id):

    cadastro = Cadastro.objects.get(id=id)
    context = {

            'cadastro': cadastro

    }
    return render(request, 'cadastro.html', context)