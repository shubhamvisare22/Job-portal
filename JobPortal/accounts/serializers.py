from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.validators import validate_email as django_validate_email
import re

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    role = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'role', 'is_active', 'is_staff', 'groups', 'user_permissions')
        read_only_fields = ('id', 'is_active', 'is_staff', 'groups', 'user_permissions')

    def validate_email(self, value):
        try:
            django_validate_email(value)
        except serializers.ValidationError as e:
            raise serializers.ValidationError("Invalid email format") from e

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")

        return value

    def validate_role(self, value):
        allowed_roles = [role[0] for role in User.USER_ROLES]
        if value not in allowed_roles:
            raise serializers.ValidationError("Invalid role")

        return value
            
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance
