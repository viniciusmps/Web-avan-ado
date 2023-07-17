from django.db import models
class Cadastro(models.Model):
    nome = models.CharField('nome',max_length=100)
    periodo = models.DateTimeField('periodo de ingresso')
    nota = models.CharField('nota',max_length=3)
    situacao = models.TextField('situação')