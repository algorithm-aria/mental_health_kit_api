from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers.text import TextSerializer
from ..serializers.image import ImageSerializer
from ..models.text import Text
from ..models.image import Image

class KitView(APIView):
    def get(self, request):
        # filter for text and images with the user's id
        texts = Text.objects.filter(owner=request.user.id)
        images = Image.objects.filter(owner=request.user.id)
        text_data = TextSerializer(texts, many=True).data
        image_data = ImageSerializer(images, many=True).data
        return Response([text_data, image_data])