from rest_framework import serializers
from .models import Chat
from django.contrib.auth.hashers import make_password

class Chatptgt(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

    def create(self, validated_data):
        try:
            user = Chat(
                nome=validated_data['nome'],
                text=validated_data['text'],
                img=validated_data['img']
            )
        except:
            user = Chat(
                nome=validated_data['nome'],
                text=validated_data['text']
            )
        user.save()
        return user
