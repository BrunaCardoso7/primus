from django.conf import settings
from django.db import models
from sugestoes.models import BaseModel


class MovimentacaoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

    def do_usuario(self, user):
        return self.get_queryset().do_usuario(user)


# Create your models here.
class Movimentacao(BaseModel):
    class IeTipoMovimentacaoChoice(models.TextChoices):
        entrada = "EN", "Entrada"
        saida = "SD", "Saida"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_movimentacao",
        null=True,
        blank=True,
    )
    produto = models.ForeignKey(
        "produtos.Produto",
        on_delete=models.CASCADE,
        related_name="produto",
        null=True,
        blank=True,
    )
    ie_tipo_movimentacao = models.CharField(
        choices=IeTipoMovimentacaoChoice.choices,
        max_length=2,
        default=IeTipoMovimentacaoChoice.entrada,
        blank=True,
        null=True,
    )
    nr_custo_unitario = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    nr_valor_total = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    nr_valor_desconto = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    nr_valor_ajuste = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    nr_valor_imposto = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    nr_valor_frete = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    dt_validade = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "movimentacao"
        verbose_name = "movimentacao"
        verbose_name_plural = "movimentacaos"
        ordering = ["-id"]

    objects = MovimentacaoManager()
    all_objects = models.Manager()
