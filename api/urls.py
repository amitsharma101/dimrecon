from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'imageupload', views.Imageuploadviewset)

urlpatterns = [
    path('', include(router.urls)),
    path('imgupload',views.myView),
]