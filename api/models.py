from django.db import models

class ImageUpload(models.Model):
    title = models.CharField(max_length=50)
    images = models.ImageField('images')