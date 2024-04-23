from django.shortcuts import render, HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from home_pi.forms import FormularioDeDenuncia
from home_pi.models import FormularioDenuncia

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