import django_filters
from django.utils import timezone
from datetime import timedelta
from .models import Produto


class ProdutosFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        field_name="ds_produto",
        lookup_expr="icontains"
    )

    ie_situacao = django_filters.ChoiceFilter(
        field_name="ie_situacao",
        choices=Produto.IeSituacaoChoice.choices,
        label="Situação"
    )

    ordering = django_filters.OrderingFilter(
        fields=(
            ('ds_produto', 'ds_produto'),
            ('nm_fornecedor', 'nm_fornecedor'),
            ('nr_total_estoque', 'nr_total_estoque'),
            ('nr_custo_unitario', 'nr_custo_unitario'),
            ('dt_validade', 'dt_validade'),
            ('id', 'id'),
        ),
        field_labels={
            'ds_produto': 'Produto',
            'nm_fornecedor': 'Fornecedor',
            'nr_total_estoque': 'Total em Estoque',
            'nr_custo_unitario': 'Custo Unitário',
            'dt_validade': 'Validade',
            'id': 'ID',
        },
        label='Ordenar por',
        empty_label=None
    )

    class Meta:
        model = Produto
        fields = []
