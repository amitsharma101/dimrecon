from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('imgupload',views.myView),
]