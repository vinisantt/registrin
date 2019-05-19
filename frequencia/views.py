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
from django.contrib.auth.models import User
import datetime



def bateponto(request):
    if request.method == 'POST':
        funci = Funcionario.objects.filter(user=request.user)
        print("aqui", funci[0].confHora.all()[0].hSaida)
        data = datetime.date.today()
        now = datetime.datetime.now().strftime('%H:%M:%S') #timezone.now()
        if Registro_Ponto.objects.filter(data=data) and Registro_Ponto.objects.filter(funcionario=funci[0]):
                print("lmafao")
        #teste = Registro_Ponto()
    return render(request, 'frequencia/timer.html')


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

   
