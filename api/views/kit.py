from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
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
    
    def post(self, request):
        request.data['owner'] = request.user.id
        key_list = request.data.keys()
        if 'body' in key_list:
            print('hamster')
            text = TextSerializer(data=request.data)
            if text.is_valid():
                text.save()
                return Response(text.data, status=status.HTTP_201_CREATED)
            else:
                return Response(text.errors, status=status.HTTP_400_BAD_REQUEST)
        elif 'image_url' in key_list:
            print('crocodile')
            image = ImageSerializer(data=request.data)
            if image.is_valid():
                image.save()
                return Response(image.data, status.HTTP_201_CREATED)
            else:
                return Response(image.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            print('sadface')

class TextView(APIView):
    def put(self, request, pk):
        request.data['owner'] = request.user.id
        text = get_object_or_404(Text, pk=pk)
        if request.user != text.owner:
            raise PermissionDenied('Unauthorized, you do not have access to this kit.')
        updated_text = TextSerializer(text, data=request.data)
        if updated_text.is_valid():
            updated_text.save()
            return Response(updated_text.data, status=status.HTTP_200_OK)
        else:
            return Response(updated_text.errors, status=status.HTTP_400_BAD_REQUEST)





        