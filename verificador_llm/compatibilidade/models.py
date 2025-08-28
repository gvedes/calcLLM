# compatibilidade/models.py
from django.db import models

class ConfiguracaoHardware(models.Model):
    nome = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100)
    gpu = models.CharField(max_length=100, blank=True, null=True)
    ram_gb = models.IntegerField()
    sistema_operacional = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class ModeloLLM(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    requisitos_hardware = models.ManyToManyField(ConfiguracaoHardware, related_name='modelos_llm')

    def __str__(self):
        return self.nome

