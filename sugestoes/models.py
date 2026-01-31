from django.db import models

# Create your models here.
class Sugestao(models.Model):
    class LikedChoice(models.TextChoices):
        YES = "sim", "Gostou"
        NO = "nao", "Não gostou"

    name = models.CharField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True)
    comment = models.CharField(null=True, blank=True)
    liked = models.CharField(
        max_length=3,
        choices=LikedChoice.choices,
        default=LikedChoice.YES
    )