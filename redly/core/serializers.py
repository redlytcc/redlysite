from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class Usercad(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            name=validated_data['name'],
            username=validated_data['username'],
            password = make_password(validated_data['password'])
        )
        user.save()
        return user
