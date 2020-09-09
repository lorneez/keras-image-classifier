from django.shortcuts import render
from rest_framework import generics

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view

from .models import User
from .serializers import UserSerializer

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        message = dict()
        if(not user_data['name'] or not user_data['email'] or not user_data['password']):
            message['message'] = 'missing fields'
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            message['message'] = 'success'
            return JsonResponse(message, status=status.HTTP_201_CREATED)
        message['message'] = 'invalid'
        return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_email = user_data['email']
        user_password = user_data['password']
        message = dict()
        if(user_email and user_password):
            user = User.objects.get(email=user_email)
            if(user_password == user.password):
                message['message'] = 'success'
                return JsonResponse(message, status=status.HTTP_201_CREATED)
            message['message'] = 'incorrect password'
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
        message['message'] = 'fields empty'
        return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
