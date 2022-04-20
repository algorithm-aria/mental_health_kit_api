from rest_framework import serializers
from ..models.text import Text
from .user import UserSerializer

class TextSerializer(serializers.ModelSerializer):
    # owner = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Text
        fields = ('id', 'title', 'body', 'attribution', 'tags', 'owner')