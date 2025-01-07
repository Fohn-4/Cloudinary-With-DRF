from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Image
from .serializers import ImageSerializer

class ImageUploadView(CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
