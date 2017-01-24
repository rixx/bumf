from rest_framework import serializers

from bumf.core.models import Dossier, RealTransaction, VirtualTransaction


class DossierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dossier
        fields = '__all__'


class VirtualTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = VirtualTransaction
        fields = '__all__'


class RealTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = RealTransaction
        fields = '__all__'
