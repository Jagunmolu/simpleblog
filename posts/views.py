from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
from posts import serializers


@api_view(http_method_names=['GET', 'POST'])
def homepage(request:Request):

    if request.method == 'POST':
        data = request.data
        response = {'message': 'Post created successfully', 'data': data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    response = {'message': 'This is a function-based view and it is only temporary.'}
    return Response(data=response, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET', 'POST'])
def list_posts(request:Request):
    posts = Post.objects.all()

    if request.method == 'POST':
        data = request.data

        serializer = PostSerializer(data=data)

        if serializer.is_valid():

            serializer.save()

            response = {'message': 'Post created successfully', 'data': serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = PostSerializer(instance=posts, many=True)

    response = {
        'message': 'All Posts',
        'data': serializer.data
    }

    return Response(data=response, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def list_post_by_id(request:Request, id:int):
    post = get_object_or_404(Post, id=id)

    serializer = PostSerializer(instance=post)

    response = {
        'message': f'Post number {id}',
        'data': serializer.data
    }


    return Response(data=response, status=status.HTTP_200_OK)

@api_view(http_method_names=['PUT'])
def update_post(request:Request, id:int):

    post = get_object_or_404(Post, id=id)

    data = request.data

    serializer = PostSerializer(instance=post, data=data)

    if serializer.is_valid():

        serializer.save()

        response = {
            'message': f'Post number {id} updated successfully',
            'data': serializer.data
        }

        return Response(data=response, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['DELETE'])
def delete_post(request:Request, id:int):

    post = get_object_or_404(Post, id=id)

    post.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
