from rest_framework import serializers

from bumf.core.models import RealAccount, VirtualAccount


class VirtualAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = VirtualAccount
        fields = '__all__'


class RealAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = RealAccount
        fields = (
            # Model fields
            'id', 'import_transactions', 'name', 'project', 'variant',
            # Properties
            'total',
        )
