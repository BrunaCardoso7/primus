from django.conf import settings
from django.db import models

from sugestoes.models import BaseModel


class ProdutoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

    def do_usuario(self, user):
        return self.get_queryset().do_usuario(user)

# Create your models here.
class Produto(BaseModel):
    class IeSituacaoChoice(models.TextChoices):
        estocado = "ES", "Estocado"
        comprar = "CP", "Comprar"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="produto",
        null=True, blank=True
    )
    ds_produto = models.CharField(max_length=255, blank=True, null=True)
    ds_observacao = models.CharField(max_length=255, blank=True, null=True)
    nm_fornecedor = models.CharField(max_length=255, blank=True, null=True)
    ie_situacao = models.CharField(choices=IeSituacaoChoice.choices, max_length=2, default=IeSituacaoChoice.estocado, blank=True, null=True)

    nr_estoque_minimo = models.IntegerField(blank=True, null=True)
    nr_total_estoque = models.IntegerField(blank=True, null=True)

    nr_custo_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nr_valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nr_valor_desconto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nr_valor_ajuste = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nr_valor_imposto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nr_valor_frete = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dt_validade = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "produto"
        verbose_name = "produto"
        verbose_name_plural = "produtos"
        ordering = ["-id"]

    objects = ProdutoManager()
    all_objects = models.Manager()