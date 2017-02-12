from rest_framework import serializers

from bumf.core.models import RealAccount, VirtualAccount


class BudgetAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = VirtualAccount
        fields = (
            # Model fields
            'id', 'name', 'project', 'parent', 'comment',
            # Properties
            'total',
            # Related fields
            'child_accounts',
        )
        depth = 10


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
