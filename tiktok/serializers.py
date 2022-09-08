from rest_framework import serializers

from .models import Auth, CallBack


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = '__all__'

class CallBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallBack
        fields = '__all__'
