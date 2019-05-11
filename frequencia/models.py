from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ConfHorario(models.Model):
    hEntrada = models.TimeField("Configuração de Horario (Entrada)", auto_now=False, auto_now_add=False)
    hSaida = models.TimeField("Configuração de Horario (Saída)", auto_now=False, auto_now_add=False)

    def __str__(self):
        return "Horário de entrada: {}  Horário de saída: {}".format(str(self.hEntrada), str(self.hSaida))

class Funcionario(models.Model):
        usuario = models.CharField(verbose_name="Nome de usuário blog",max_length = 128)
        nome = models.CharField(verbose_name="Nome Completo", max_length = 128)
        data_de_nascimento = models.CharField(
            'Data de nascimento', blank=True, null=True,max_length = 128)
        chefe = models.ForeignKey("Funcionario",blank=True, null=True,verbose_name="AAA", on_delete=models.CASCADE)
        confHora = models.ManyToManyField(ConfHorario, verbose_name="Horarios")
        
        def __str__(self):
            return self.nome

class Justificativa(models.Model):
    def __str__(self):
        return self.conteudo

    conteudo = models.TextField()
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    
