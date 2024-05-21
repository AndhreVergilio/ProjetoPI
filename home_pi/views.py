from django.shortcuts import render, redirect, HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from home_pi.forms import FormularioDeDenuncia
from home_pi.models import FormularioDenuncia
from django.contrib.auth import authenticate, login

# Create your views here.
@csrf_exempt
def home (request):
    template = loader.get_template('base.html')
    
    if request.method == 'POST':
        form = FormularioDeDenuncia(request.POST)

        print(form.errors)
        if form.is_valid():
            print('Salvando formulario na database')
            temp = FormularioDenuncia()
            temp.Nome = request.POST.get('Nome', 'None')
            temp.Localizacao = request.POST.get('Localizacao', 'None')
            temp.Opcao = request.POST.get('Opcao', 'None')
            temp.Descricao = request.POST.get('Descricao', 'None')
            temp.save()

    return HttpResponse(template.render()) 


def index (request):
    template = loader.get_template('index.html')
    return render(request, 'index.html')

def main (request):
    template = loader.get_template('')


# Formulário de cadastro de usuário
def cadastro (request):
    return render(request, 'cadastro.html')
    # return render(request, 'create.html')
    # if(request.POST['password'] != request.POST['password-conf']):
    #          data['msg'] = 'Senha e confirmação de senha diferentes!'
    #          data['class'] = 'alert-danger'
        #  else:
        #      user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        #      user.first_name = request.POST['name']
        #      user.save()
        #      data['msg'] = 'Usuário cadastrado com sucesso!'
        #      data['class'] = 'alert-success'
    # return render(request,'create.html',data)

# Enviar dados para o banco

# Página do grupo
def equipe (request):
    return render(request, 'equipe.html')

def store (request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    return render(request, 'index.html',data)
    

# Formulário do painel do Login
def login (request):
    return render(request, 'login.html')

def bcoDado (request):
    return render(request, 'login.html')
    

# Processamento de Login
def dologin (request):
    user = authenticate(username=request.POST['email'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        return render(request, 'base.html')
    

def dashboard (request):
    return render(request, '/dashboard/login.html')