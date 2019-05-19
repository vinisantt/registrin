from django.contrib import admin
from .models import ConfHorario, Funcionario, Justificativa, Registro_Ponto,Status

# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Justificativa)
admin.site.register(ConfHorario)
admin.site.register(Status)

@admin.register(Registro_Ponto)
class Registro_PontoAdmin(admin.ModelAdmin):
        readonly_fields = ["ip", "entrada", "saida"]

