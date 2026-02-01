import django_filters
from django.utils import timezone
from datetime import timedelta
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

    periodo = django_filters.ChoiceFilter(
        method='filter_periodo',
        choices=(
            ('hoje', 'Hoje'),
            ('semana', 'Esta semana'),
            ('mensal', 'Este mês'),
        ),
        label='Período'
    )

    ordering = django_filters.OrderingFilter(
        fields=(
            ('hr_agendamento', 'hr_agendamento'),
            ('is_finalizado', 'is_finalizado'),
        ),
        field_labels={
            'hr_agendamento': 'Horário Agendamento',
            'is_finalizado': 'Finalizado'
        },
        label='Ordenar por',
        empty_label=None
    )

    class Meta:
        model = Carro
        fields = [
            "nm_cliente",
            "nr_placa",
            "is_finalizado",
            "ie_tipo_lavagem",
        ]

    def filter_periodo(self, queryset, name, value):
        hoje = timezone.now().date()
        if value == 'hoje':
            return queryset.filter(created_at__date=hoje)
        elif value == 'semana':
            inicio_semana = hoje - timedelta(days=hoje.weekday())
            fim_semana = inicio_semana + timedelta(days=6)
            return queryset.filter(created_at__date__range=(inicio_semana, fim_semana))
        elif value == 'mensal':
            inicio_mes = hoje.replace(day=1)
            return queryset.filter(created_at__date__gte=inicio_mes)
        return queryset

    @property
    def qs(self):
        return super().qs.order_by('hr_agendamento')
