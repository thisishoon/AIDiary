from django.shortcuts import render
from rest_framework.response import Response

from .models import Diary
from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DiarySerializer
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
import random, string
from django.contrib.auth import login, authenticate
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt



class DiaryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Diary.objects.all()
    serializer_class = DiarySerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Diary.objects.all()
        else:
            return Diary.objects.filter(user=user)# , many=True)

    def create(self, request, **kwargs):
        content = request.data["content"]
        user = request.user.id
        #여기서 content를 통해 감정도를 넣으면 됌
        feeling = 100

        serializer = DiarySerializer(data={"content": content, "user": user, "happiness": feeling})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        content = request.data["content"]
        user = request.user.id
        Diary.objects.filter(id=pk).update(content=content)

        return JsonResponse({"content": content})

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user',)



