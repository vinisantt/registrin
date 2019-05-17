from django.contrib import admin
from .models import ConfHorario, Funcionario, Justificativa, Registro_Ponto

# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Justificativa)
admin.site.register(ConfHorario)

@admin.register(Registro_Ponto)
class Registro_PontoAdmin(admin.ModelAdmin):
        readonly_fields = ["ip", "entrada"]
