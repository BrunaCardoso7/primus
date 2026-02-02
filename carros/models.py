from sugestoes.models import BaseModel
from django.db import models
from django.conf import settings


class CarroManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

    def do_usuario(self, user):
        return self.get_queryset().do_usuario(user)


class Carro(BaseModel):
    class TipoLavagemChoice(models.TextChoices):
        simples = "SP", "Simples"
        completa = "CP", "Completa"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="carros",
        null=True, blank=True
    )
    nm_carro = models.CharField(null=True, blank=True)
    nr_placa = models.CharField(null=True, blank=True)
    nm_cliente = models.CharField(null=True, blank=True)
    nr_telefone_cliente = models.CharField(null=True, blank=True)
    hr_agendamento = models.TimeField(null=True, blank=True)
    ds_observacao = models.CharField(null=True, blank=True)
    nr_valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    is_finalizado = models.BooleanField(default=False, null=True, blank=True)
    ie_tipo_lavagem = models.CharField(
        max_length=3,
        choices=TipoLavagemChoice.choices,
        default=TipoLavagemChoice.simples
    )

    objects = CarroManager()
    all_objects = models.Manager()