from rest_framework import serializers
from .models import User
from .models import Image

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'email',
            'password',
        )
        model = User

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'file',
        )
        model = Image
