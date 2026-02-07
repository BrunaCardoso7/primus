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
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="produto",
        null=True, blank=True
    )
    nm_produto = models.CharField(max_length=255)
    cd_barras = models.CharField(max_length=13, unique=True, db_index=True)
    vl_venda = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)

    class Meta:
        db_table = "produto"
        verbose_name = "produto"
        verbose_name_plural = "produtos"
        ordering = ["-id"]

    objects = ProdutoManager()
    all_objects = models.Manager()