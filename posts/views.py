from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from .models import Post
from .serializers import PostSerializer


@api_view(http_method_names=['GET', 'POST'])
def homepage(request:Request):
    if request.method == 'POST':
        data = request.data
        response = {'message': 'Post created successfully', 'data': data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    response = {'message': 'This is a function-based view and it is only temporary.'}
    return Response(data=response, status=status.HTTP_200_OK)

class PostListCreateView(APIView):
    serializer_class = PostSerializer
    def get(self, request:Request):
        posts = Post.objects.all()
        serializer = self.serializer_class(instance=posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Post created successfully.',
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostRetrieveUpdateDeleteView(APIView):
    serializer_class = PostSerializer
    def get(self, request:Request, id:int):
        post = get_object_or_404(Post, id=id)
        serializer = self.serializer_class(instance=post)
        response = {
            'message': f'Post number {id}',
            'data': serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)

    def put(self, request:Request, id:int):
        post = get_object_or_404(Post, id=id)
        serializer = self.serializer_class(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': f'Post number {id} updated successfully',
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request:Request, id:int):
        post = get_object_or_404(Post, id=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
