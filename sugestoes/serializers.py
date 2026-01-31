from rest_framework import serializers
from .models import *

class SugestaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sugestao
        fields = "__all__"
