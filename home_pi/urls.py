from django.urls import path
from . import views 
from home_pi.views import index, cadastro, bcoDado, login, dologin, dashboard, equipe


urlpatterns = [
    path('', views.login, name='login'),
    path('', views.home, name='home'),
    path('cadastro/', cadastro),
    #path('bcoDado/', bcoDado),
    path('login/', login),
    path('dologin/', dologin),
    path('dashboard/', dashboard),
    path('equipe/', equipe),  
]