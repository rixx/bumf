from rest_framework import serializers

from bumf.api.serializers.account import (
    RealAccountSerializer, VirtualAccountSerializer,
)
from bumf.core.models import Dossier, RealTransaction, VirtualTransaction


class DossierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dossier
        fields = '__all__'


class VirtualTransactionSerializer(serializers.ModelSerializer):
    destination = VirtualAccountSerializer()
    source = VirtualAccountSerializer()

    class Meta:
        model = VirtualTransaction
        fields = '__all__'


class RealTransactionSerializer(serializers.ModelSerializer):
    destination = RealAccountSerializer
    source = RealAccountSerializer
    transactions = VirtualTransactionSerializer(many=True)

    class Meta:
        model = RealTransaction
        fields = (
            # Model fields
            'dossier', 'source', 'destination', 'amount', 'timestamp',
            # Related fields
            'transactions',
        )
