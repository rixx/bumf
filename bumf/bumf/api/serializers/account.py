from rest_framework import serializers

from bumf.core.models import Project, RealAccount, VirtualAccount


class VirtualAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = VirtualAccount
        fields = '__all__'


class RealAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = RealAccount
        fields = '__all__'
