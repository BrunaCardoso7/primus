from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Movimentacao
from .serializers import MovimentacaoSerializer
from .filters import MovimentacaoFilter


class MovimentacaoViewSet(ModelViewSet):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer
    http_method_names = ["get", "post", "patch", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovimentacaoFilter

    def get_permissions(self):
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
