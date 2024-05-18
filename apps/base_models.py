from django.db import models

class BaseModels(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Data de atualizado')

    class Meta:
        abstract = True