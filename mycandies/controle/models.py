# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import os


class Vendas(models.Models):

    cliente = models.CharField(max_length=200, blank=False)
    produto = models.CharField(max_length=100, blank=False)
    data_compra = models.DateTimeField(default=timezone.now)
    valor_produto = models.FloatField(default=0.0)
    valor_divida =  models.FloatField(default=0.0)
    foto = models.ImageField('Produto', upload_to='media/photo')
    data_quitacao = models.DateTimeField('Date', auto_now=False, auto_now_add=False)

    def __unicode__(self):
        return '%s - %.2f' % (self.cliente, self.valor_divida)

    def soma_divida(self, valor_produto, valor_divida):
        if valor_divida != 0:
            valor_divida = valor_divida + valor_produto
        return (valor_divida)
    
    class Meta:
        ordering = ('-data_compra', )
