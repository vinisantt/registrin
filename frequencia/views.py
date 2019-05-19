from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView, FormView,TemplateView
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.views.generic import ListView, FormView,TemplateView
from django.http import *


def bateponto(request):
    return render(request,'frequencia/index.html'
)