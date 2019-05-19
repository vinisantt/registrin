from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro_batida/',bateponto,name='ponto')
]
