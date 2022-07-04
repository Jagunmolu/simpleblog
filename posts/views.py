from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, mixins, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostSerializer


# class PostViewset(viewsets.ModelViewSet):
#     authentication_classes = [IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostListCreateView(generics.ListCreateAPIView):

    serializer_class = PostSerializer
    permission_classes = []
    queryset = Post.objects.all()

    # def get(self, request:Request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

        
    # def post(self, request:Request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = PostSerializer
    permission_classes = []
    queryset = Post.objects.all()
    
    # def put(self, request:Request, *args, **kwargs):
    #     pass

    # def get(self, request:Request, *args, **kwargs):
    #     pass

    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)