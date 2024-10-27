from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Job

# Serializer for the Job model
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'  # You can list specific fields if needed
        read_only_fields = ['posted_by']  # Make 'posted_by' read-only to prevent it from being set by the client

# Serializer for User registration
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}  # Ensure the password is write-only
        }

    def create(self, validated_data):
        # Create a user instance while ensuring the password is hashed
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email'),  # Email can be optional
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()  # Save the user instance
        return user
