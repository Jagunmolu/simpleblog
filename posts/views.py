from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Post
from .serializers import PostSerializer
from posts import serializers


# class PostListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     def get(self, request:Request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request:Request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



# class PostRetrieveUpdateDeleteView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     def get(self, request:Request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request:Request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request:Request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


class PostViewset(viewsets.ViewSet):
    def list(self, request:Request):
        queryset = Post.objects.all()
        serializer = PostSerializer(instance=queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request:Request, pk:int):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
