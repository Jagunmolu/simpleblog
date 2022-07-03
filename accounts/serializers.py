from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError
from .models import User


class SignUpSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    username = serializers.CharField(max_length=15)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:

        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):

        email_exists = User.objects.filter(email=attrs['email']).exists()
        username_exists = User.objects.filter(username=attrs['username']).exists()

        if email_exists and username_exists:
            raise ValidationError('Email and Username have been used')
        if email_exists:
            raise ValidationError('Email has been used')
        if username_exists:
            raise ValidationError('Username has been used')
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user