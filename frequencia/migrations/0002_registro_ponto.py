# Generated by Django 2.2 on 2019-05-11 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frequencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_Ponto',
            fields=[
                ('entrada', models.DateTimeField(auto_now_add=True, verbose_name='Horário de Entrada')),
                ('saida', models.DateTimeField(auto_now_add=True, verbose_name='')),
                ('ip', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ip da Funcionario')),
                ('funcionario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='frequencia.Funcionario')),
            ],
        ),
    ]
