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
        data = datetime.datetime.now().strftime('%Y-%m-%d')
        now = datetime.datetime.now().strftime('%H:%M:%S') #timezone.now()
        #Caso já exista o registro ele só adiciona a saida como segundo.

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
        else:
                ip = request.META.get('REMOTE_ADDR')

        if Registro_Ponto.objects.filter(data=data, funcionario=funci[0]).exists() == False:
                print("lmao dude yes")
                (now_h, now_m, now_s) = now.split(':')
                total = int(now_h) * 3600 + int(now_m) * 60 + int(now_s)
                (saida_h, saida_m, saida_s) = str(funci[0].confHora.all()[0].hSaida).split(':')
                total_saida = int(saida_h) * 3600 + int(saida_m) * 60 + int(saida_s)
                if (total_saida - total) > 900:
                        ponto_agora = Registro_Ponto(data=data)
                        ponto_agora.status=Status.objects.filter(nome="INCONSISTENTE")[0]
                        ponto_agora.entrada=str(now) 
                        ponto_agora.funcionario=funci[0]
                        ponto_agora.ip = ip
                        ponto_agora.save()
                else:
                        ponto_agora = Registro_Ponto(data=data)
                        ponto_agora.status=Status.objects.filter(nome="CONSISTENTE")[0]
                        ponto_agora.entrada=str(now) 
                        ponto_agora.funcionario=funci[0]
                        ponto_agora.ip = ip
                        ponto_agora.save()
        elif Registro_Ponto.objects.filter(data=data, funcionario=funci[0])[0].saida is None:
                print("saidera men", Registro_Ponto.objects.filter(data=data, funcionario=funci[0])[0].saida)
                (now_h, now_m, now_s) = now.split(':')
                total = int(now_h) * 3600 + int(now_m) * 60 + int(now_s)
                (saida_h, saida_m, saida_s) = str(funci[0].confHora.all()[0].hSaida).split(':')
                total_saida = int(saida_h) * 3600 + int(saida_m) * 60 + int(saida_s)
                ponto_agora = Registro_Ponto.objects.filter(data=data, funcionario=funci[0])[0]
                #Caso seja maior que 15 minutos ele atribui inconsistente
                if (total_saida - total) > 900:
                    ponto_agora.saida=str(now) 
                    ponto_agora.status=Status.objects.filter(nome="INCONSISTENTE")[0]
                    ponto_agora.save()
                else:
                    ponto_agora.saida=str(now) 
                    ponto_agora.status=Status.objects.filter(nome="CONSISTENTE")[0]
                    ponto_agora.save()
                    print("nem foi man")
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

   
