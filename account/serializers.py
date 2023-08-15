from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'password_confirm']

    def validate(self, attrs):
        if attrs.get('password') != attrs.pop('password_confirm'):
            raise serializers.ValidationError('password does not match')

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)

        return user
