from django.shortcuts import render

# Create your views here.
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsPostOwner

class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

class PostDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            self.permission_classes = [IsPostOwner] #비번 맞는지 확인
        else: 
            self.permission_classes = []
        return super(PostDetailAPIView, self).get_permissions()    