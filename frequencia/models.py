from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class ConfHorario(models.Model):
    descricao= models.CharField("Descrição", max_length=120)
    hEntrada = models.TimeField("Configuração de Horario (Entrada)", auto_now=False, auto_now_add=False)
    hSaida = models.TimeField("Configuração de Horario (Saída)", auto_now=False, auto_now_add=False)

    def __str__(self):
        return "{} | Horário de entrada: {}  Horário de saída: {}".format(self.descricao, str(self.hEntrada), str(self.hSaida))


class Funcionario(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        birth_date = models.DateField(null=True, blank=True)
        chefe = models.ForeignKey("Funcionario",blank=True, null=True,verbose_name="Superior", on_delete=models.CASCADE)
        confHora = models.ManyToManyField(ConfHorario, verbose_name="Horarios")

        def __str__(self):
            return self.user.username

class Justificativa(models.Model):
    def __str__(self):
        return self.conteudo

    conteudo = models.TextField()
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

class Status(models.Model):
    nome = models.CharField("Status",max_length=15)
    
    def __str__(self):
        return self.nome

class Registro_Ponto(models.Model):
    class Meta:
        verbose_name = 'Registro de Ponto'
        verbose_name_plural= 'Registros de Ponto'

    data = models.DateField(null=True, blank=True)

    entrada= models.DateTimeField(verbose_name= "Entrada", 
        auto_now_add=True,
        )
    saida= models.DateTimeField(verbose_name= "Saída", 
        auto_now_add=True,
        )
    ip= models.CharField(verbose_name="Ip do Funcionario", 
        max_length=15, 
        blank=True, 
        null=True,
        )
    status= models.ForeignKey(Status, 
        on_delete=models.CASCADE,
        verbose_name= "Status do Funcionário",
        blank=True, 
        null=True,
        )
    funcionario= models.OneToOneField(Funcionario, 
        on_delete=models.CASCADE,
        primary_key=True,
        )


    def __str__(self):
        return self.funcionario.nome


