from rest_framework import serializers
from .models import Sugestao


class SugestaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sugestao
        exclude = ("user",)
