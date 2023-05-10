from django.db import models
from django.urls import reverse


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    data_de_nascimento = models.DateField()
    telefone = models.CharField()

    def __str__(self) -> str:
        return f'{self.nome}, {self.email}, {self.data_de_nascimento}, {self.telefone}'

    def get_absolute_url(self):
        return reverse('detalhes', kwargs={'cliente_id': self.pk})
