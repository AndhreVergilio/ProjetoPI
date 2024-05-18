from django.db import models

# Create your models here.

class FormularioDenuncia(models.Model):

    Nome = models.CharField(max_length=50)
    Localizacao = models.CharField(max_length=50)
    Opcao = models.CharField(max_length=50)
    Descricao = models.CharField(max_length=250)
    Foto = models.ImageField(upload_to='fotos_denuncias/', default='media/osint.png')
    Latitude = models.FloatField(max_length=250, default=None, null=True)
    Longitude = models.FloatField(max_length=250, default=None, null=True)


    def __str__(self) -> str:
        return self.Nome