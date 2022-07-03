from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostSerializer


class PostViewset(viewsets.ModelViewSet):
    authentication_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
