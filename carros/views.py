from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .filters import CarroFilter
from .models import Carro
from .serializers import CarroSerializer


class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    permission_classes = [AllowAny]
    filterset_class = CarroFilter
    ordering_fields = ['hr_agendamento', 'is_finalizado']
    ordering = ['hr_agendamento']
    http_method_names = ['get', 'post', 'patch', "delete"]
    def get_permissions(self):
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)