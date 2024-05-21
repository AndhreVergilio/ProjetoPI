from django.db import models

# Create your models here.

class FormularioDenuncia(models.Model):

    Nome = models.CharField(max_length=50)
    Localizacao = models.CharField(max_length=50)
    Opcao = models.CharField(max_length=50)
    Descricao = models.CharField(max_length=250)
    Foto = models.ImageField(upload_to='Fotos_denuncia/', default=None, unique=True)


    def __str__(self) -> str:
        return self.Nome