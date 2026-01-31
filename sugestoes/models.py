from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()


class Sugestao(BaseModel):
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