from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.db.models import Sum

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

    @action(detail=False, methods=['get'], url_path='total')
    def total(self, request):

        queryset = self.filter_queryset(self.get_queryset())

        total = queryset.aggregate(
            total_valor=Sum('nr_valor')
        )['total_valor'] or 0

        return Response({
            'total': total
        })