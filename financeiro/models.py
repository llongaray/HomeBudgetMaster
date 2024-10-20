from django.db import models

# Create your models here.

class Gasto(models.Model):
    nome = models.CharField(max_length=100)
    tipo_gasto = models.CharField(max_length=50)
    tipo_local = models.CharField(max_length=50)
    tipo_quem = models.CharField(max_length=50)
    entrada_saida = models.CharField(max_length=10)  # 'entrada' ou 'saída'
    status = models.CharField(max_length=20)  # Ex: 'pendente', 'concluído'
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
