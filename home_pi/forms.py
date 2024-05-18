from django import forms

class FormularioDeDenuncia(forms.Form):
        
    Nome = forms.CharField(max_length=50)
    Localizacao = forms.CharField(max_length=50)
    Opcao = forms.CharField(max_length=50)
    Descricao = forms.CharField(max_length=250)
    Foto = forms.ImageField(required=False)