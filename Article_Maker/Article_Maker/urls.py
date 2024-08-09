from django.urls import include, path
from rest_framework import routers

from main import views

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include("main.urls")),
]
