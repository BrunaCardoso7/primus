from rest_framework import serializers

from movimentacao.models import Movimentacao
from .models import *
from django.db import transaction


class ProdutoSerializer(serializers.ModelSerializer):
    ie_tipo_movimentacao = serializers.CharField(write_only=True)
    usto_unitario = serializers.DecimalField(max_digits=10, decimal_places=2, write_only=True, required=False,
                                             allow_null=True)
    nr_valor_total = serializers.DecimalField(max_digits=10, decimal_places=2, write_only=True, required=False,
                                              allow_null=True)
    nr_valor_desconto = serializers.DecimalField(max_digits=10, decimal_places=2, write_only=True, required=False,
                                                 allow_null=True)
    nr_valor_ajuste = serializers.DecimalField(max_digits=10, decimal_places=2, write_only=True, required=False,
                                               allow_null=True)
    nr_valor_imposto = serializers.DecimalField(max_digits=10, decimal_places=2, write_only=True, required=False,
                                                allow_null=True)
    nr_valor_frete = serializers.DecimalField(max_digits=10, decimal_places=2, write_only=True, required=False,
                                              allow_null=True)
    dt_validade = serializers.DateTimeField(write_only=True, required=False, allow_null=True)

    @transaction.atomic
    def create(self, validated_data):
        tipo = validated_data.pop("ie_tipo_movimentacao")
        custo = validated_data.pop("nr_custo_unitario", None)
        total = validated_data.pop("nr_valor_total", None)
        desconto = validated_data.pop("nr_valor_desconto", None)
        ajuste = validated_data.pop("nr_valor_ajuste", None)
        imposto = validated_data.pop("nr_valor_imposto", None)
        frete = validated_data.pop("nr_valor_frete", None)
        validade = validated_data.pop("dt_validade", None)

        produto = Produto.objects.create(**validated_data)

        Movimentacao.objects.create(
            produto=produto,
            ie_tipo_movimentacao=tipo,
            nr_custo_unitario=custo,
            nr_valor_total=total,
            nr_valor_desconto=desconto,
            nr_valor_ajuste=ajuste,
            nr_valor_imposto=imposto,
            nr_valor_frete=frete,
            dt_validade=validade,
        )

        return produto

    class Meta:
        model = Produto
        fields = "__all__"
