from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from main.serializers import GroupSerializer, UserSerializer

import google.generativeai as genai
import os
from rest_framework.views import APIView
from rest_framework.response import Response

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class Articles(APIView):

    def post(self, request, format=None):
        prompt = f"I want an article for {request.data['prompt']}, this article should be {request.data['tone']}, and the length should be {request.data['length']}, as a html post"
        response = model.generate_content(prompt)
        return Response(response.text)
