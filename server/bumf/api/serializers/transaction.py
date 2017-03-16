from django.db import transaction
from rest_framework import serializers

from bumf.api.serializers.account import (
    RealAccountSerializer, VirtualAccountSerializer,
)
from bumf.core.models import (
    Dossier, Project, RealTransaction, VirtualAccount, VirtualTransaction,
)


class DossierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dossier
        fields = '__all__'


class VirtualTransactionReadSerializer(serializers.ModelSerializer):
    destination = VirtualAccountSerializer()
    source = VirtualAccountSerializer()

    class Meta:
        model = VirtualTransaction
        fields = [
            'dossier', 'source', 'destination', 'bank_transaction',
            'amount', 'comment', 'timestamp',
        ]


class VirtualTransactionWriteSerializer(serializers.ModelSerializer):
    destination = serializers.SlugRelatedField(slug_field='name', queryset=VirtualAccount.objects.all())
    source = serializers.SlugRelatedField(slug_field='name', queryset=VirtualAccount.objects.all())

    class Meta:
        model = VirtualTransaction
        fields = [
            'source', 'destination', 'bank_transaction',
            'amount', 'comment', 'timestamp',
        ]


class RealTransactionReadSerializer(serializers.ModelSerializer):
    destination = RealAccountSerializer
    dossier = DossierSerializer
    source = RealAccountSerializer
    transactions = VirtualTransactionReadSerializer(many=True)

    class Meta:
        model = RealTransaction
        fields = (
            # Model fields
            'dossier', 'source', 'destination', 'amount', 'timestamp',
            # Related fields
            'transactions',
        )


class RealTransactionWriteSerializer(serializers.ModelSerializer):
    transactions = VirtualTransactionWriteSerializer(many=True)
    dossier = DossierSerializer()

    def create(self, validated_data):
        with transaction.atomic():
            dossier = validated_data.pop('dossier')
            transactions = validated_data.pop('transactions')
            instance = RealTransaction.objects.create(
                dossier=dossier,
                **validated_data,
            )
            for trans in transactions:
                VirtualTransaction.objects.create(
                    bank_transaction=instance,
                    dossier=dossier,
                    **trans,
                )
            return instance

    def validate_dossier(self, value):
        return Dossier.objects.create(project=value['project'])

    class Meta:
        model = RealTransaction
        fields = (
            # Model fields
            'dossier', 'source', 'destination', 'amount', 'timestamp',
            # Related fields
            'transactions',
        )
