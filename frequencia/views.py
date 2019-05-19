from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView, FormView,TemplateView
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.views.generic import ListView, FormView,TemplateView
from django.http import *
from django.utils import timezone
from .models import *



def bateponto(request):
    if request.method == 'POST':
        now = timezone.now()
        teste = Registro_Ponto()
        
def chefeView(request,funcionario_id):
    try:
        funcionario = Funcionario.objects.get(pk = funcionario_id)
        subordinados = Funcionario.objects.filter(chefe = funcionario)
        pontos = Registro_Ponto.objects.all()

        if funcionario.chefe == None:
                return render(request, 'frequencia/chefe.html', {'chefe':funcionario,'subordinados':subordinados,'pontos':pontos})

    except Funcionario.DoesNotExist:
        raise Http404('Funcionario não encontrada')


def testeView(request):
        
        funcionarios = Funcionario.objects.all()

        return render(request, 'frequencia/funcionarios.html', {'funcionarios':funcionarios})

   
