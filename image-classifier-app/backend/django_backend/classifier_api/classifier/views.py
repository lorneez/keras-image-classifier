from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet

import os
import json
import math
import numpy as np
import matplotlib.pyplot as plt

from werkzeug.utils import secure_filename
from keras.models import load_model
from skimage.transform import resize

from .models import User
from .models import Image

from .forms import ImageForm

from .serializers import UserSerializer
from .serializers import ImageSerializer

UPLOAD_FOLDER = 'uploads/'
global model
model = load_model('classifier/cifar10_model/cifar.h5')

class Users(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Images(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

@api_view(['POST'])
def register(request):
    message = dict()
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        if(not user_data['name'] or not user_data['email'] or not user_data['password']):
            message['message'] = 'missing fields'
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            message['message'] = 'registration successful'
            return JsonResponse(message, status=status.HTTP_201_CREATED)
        message['message'] = 'invalid registration'
        return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
    message['message'] = 'not a post request'
    return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    message = dict()
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_email = user_data['email']
        user_password = user_data['password']
        if(user_email and user_password):
            user = User.objects.get(email=user_email)
            if(user_password == user.password):
                message['message'] = 'login successful'
                return JsonResponse(message, status=status.HTTP_201_CREATED)
            message['message'] = 'incorrect password'
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
        message['message'] = 'fields empty'
        return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
    message['message'] = 'not a post request'
    return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def predict(request):
    message = dict()
    if request.method == 'POST':
        form = ImageForm(request.FILES)
        if form.is_valid():
            newImage = Image(file = request.FILES['file'])
            newImage.save()
            image = saveAndResize(request.FILES['file'].name)
            probabilities = model.predict(np.array([image, ]))[0, :]
            message['message'] = 'prediction successful'
            message['predictions'] = generatePrediction(probabilities)
            return JsonResponse(message, status=status.HTTP_201_CREATED)
        print(form.errors)
        message['message'] = 'invalid file'
        return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
    message['message'] = 'not a post request'
    return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)

def generatePrediction(probabilities):
      number_to_class = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
      for i in range(10):
              print(number_to_class[i], probabilities[i])
      index = np.argsort(probabilities)
      predictions = {
        "class1": number_to_class[index[9]],
        "prob1": math.trunc(np.float64(probabilities[index[9]]) * 100),
      }
      return predictions

def saveAndResize(file):
    my_image = plt.imread(os.path.join('uploads', file))
    my_image_re = resize(my_image, (32, 32, 3))
    my_image_re = my_image_re.astype('float32')
    # my_image_re = my_image_re / 255
    return my_image_re
