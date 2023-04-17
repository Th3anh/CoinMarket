from rest_framework import serializers
from user_management.models import Web3User
from .models import *


class Web3UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Web3User
        fields = '__all__'


class TokenSerializer(serializers.ModelSerializer):
    click_link = serializers.StringRelatedField(many=True)
    class Meta:
        model = BNB
        fields = ["click_link",]