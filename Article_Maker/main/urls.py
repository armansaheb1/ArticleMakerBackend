from django.urls import include, path
from rest_framework import routers

from main import views

app_name = "main"
urlpatterns = [
    path("articles", views.Articles.as_view()),
]
