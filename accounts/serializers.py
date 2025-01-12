from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.contrib.auth import authenticate
from accounts.models import CustomUser


class UserSignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data["email"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid email or password.")
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")
        return {"user": user}


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'display_name', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            display_name=validated_data['display_name'],
            password=validated_data['password']
        )
        # Generate tokens for the user
        refresh = RefreshToken.for_user(user)
        return {
            'user': user,
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class CustomUserSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'display_name',
            'image_url',
            'accounts',
            'response_time',
            'rating',
            'job_success_rate',
            'skills',
            'categories',
        ]

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            image_url = obj.image.url
            if request is not None:
                return request.build_absolute_uri(image_url)
            return f"{settings.MEDIA_URL}{image_url}"
        return None
