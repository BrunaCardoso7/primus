from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Sugestao
from .serializers import SugestaoSerializer


class SugestaoViewSet(ModelViewSet):
    queryset = Sugestao.objects.all()
    serializer_class = SugestaoSerializer
    http_method_names = ['get', 'post']
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

