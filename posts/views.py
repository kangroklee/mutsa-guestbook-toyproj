from django.shortcuts import render

# Create your views here.
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [] #비번 맞는지 확인
    queryset = Post.objects.all()
    serializer_class = PostSerializer