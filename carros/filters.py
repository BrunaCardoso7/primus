import django_filters
from .models import Carro


class CarroFilter(django_filters.FilterSet):
    nm_cliente = django_filters.CharFilter(
        field_name="nm_cliente",
        lookup_expr="icontains"
    )

    nr_placa = django_filters.CharFilter(
        field_name="nr_placa",
        lookup_expr="icontains"
    )

    is_finalizado = django_filters.BooleanFilter()

    ie_tipo_lavagem = django_filters.CharFilter()

    data_agendamento = django_filters.TimeFilter(
        field_name="hr_agendamento"
    )

    ordering = django_filters.OrderingFilter(
        fields=(
            ('hr_agendamento', 'hr_agendamento'),
            ('is_finalizado', 'is_finalizado'),
        ),
        field_name='ordenar_por',
        label='Ordenar por'
    )

    class Meta:
        model = Carro
        fields = [
            "nm_cliente",
            "nr_placa",
            "is_finalizado",
            "ie_tipo_lavagem",
        ]
