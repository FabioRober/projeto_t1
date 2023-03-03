from django.db import models
'''formulario - colunas_banco_dados'''


class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
