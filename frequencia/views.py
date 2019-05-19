from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView, FormView,TemplateView
from django.contrib.auth import authenticate, login
from .forms import LoginForm

class CadastroSucessoView(TemplateView):
    template_name = 'registration/login.html'
