from rest_framework import serializers
from ..models.image import Image
from .user import UserSerializer

class ImageSerializer(serializers.ModelSerializer):
    # owner = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Image
        fields = ('id', 'title', 'image_url', 'tags', 'owner')