from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import SignUpSerializer


class SignUpView(generics.GenericAPIView):

    serializer_class = SignUpSerializer

    def post(self, request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        response = {
            'message': 'User has been created successfully',
            'data': serializer.data
        }

        if serializer.is_valid():
            serializer.save()
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
