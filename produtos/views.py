from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Produto
from .serializers import ProdutoSerializer
from .filters import ProdutosFilter


class ProdutosViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    http_method_names = ["get", "post", "patch", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProdutosFilter

    def get_permissions(self):
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
