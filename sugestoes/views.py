from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Sugestao
from .serializers import SugestaoSerializer


class SugestaoViewSet(ModelViewSet):
    queryset = Sugestao.objects.all()
    serializer_class = SugestaoSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'post']
