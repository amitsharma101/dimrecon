from django.shortcuts import render
from rest_framework import viewsets
from .models import ImageUpload
from .serializers import ImageUploadSerializer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .maindimenfile import dim

from dimrecon.settings import MEDIA_ROOT
import os

class Imageuploadviewset(viewsets.ModelViewSet):
   queryset = ImageUpload.objects.all()
   serializer_class = ImageUploadSerializer

   def post(self,request):
      print(self.request.data)

@csrf_exempt
def myView(request):
   print(request.FILES)
   img = request.FILES['image']
   print(img)
   print(type(img))
   print((request.POST['width']))
   width = request.POST['width']
   handle_uploaded_file(img)
   dim("abc.jpg",float(width))

   return JsonResponse({
      'newimage':os.path.join(MEDIA_ROOT,'aaa.jpg')
   })

def handle_uploaded_file(f):
    with open('abc.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
