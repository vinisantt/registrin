from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views
from frequencia.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro_batida/', TemplateView.as_view(template_name='frequencia/timer.html'), name='logout'),
    path('chefe/<int:funcionario_id>', chefeView, name = 'chefe'),
    ]
