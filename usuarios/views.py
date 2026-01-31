from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UsuarioSerializer


class SugestaoViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'post', 'patch']
