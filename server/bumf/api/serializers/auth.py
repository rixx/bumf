from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from bumf.core.models import User


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)

        user.set_password(password)
        user.save(update_fields=['password'])
        return user

    def update(self, validated_data):
        if 'password' in validated_data:
            raise ValidationError(
                {'password': 'Please use the web frontend to change your password.'}
            )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'id', 'nick', 'password']
