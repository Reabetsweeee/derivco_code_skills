from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    """handle user registration and password validation"""
   
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ('id','username', 'email', 'password', 'bio', 'github_url', 'google_url', 'linkedin_url', 'avatar')

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            bio=validated_data.get('bio', ''),
            github_url=validated_data.get('github_url', ''),
            google_url=validated_data.get('google_url', ''),
            linkedin_url=validated_data.get('linkedin_url', ''),
            avatar=validated_data.get('avatar', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    """handle user profile updates"""

    class Meta:
        model = CustomUser
        fields = ('id','username', 'email', 'bio', 'github_url', 'google_url', 'linkedin_url', 'avatar')
        read_only_fields = ('username', 'email')