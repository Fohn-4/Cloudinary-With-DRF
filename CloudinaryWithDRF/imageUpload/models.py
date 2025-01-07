from django.db import models
from cloudinary.models import CloudinaryField

class Image(models.Model):
    imageFile = CloudinaryField('image', folder='exmple/')