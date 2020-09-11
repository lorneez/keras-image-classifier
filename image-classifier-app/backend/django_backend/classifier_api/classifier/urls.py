from django.urls import path

from . import views

urlpatterns = [
    path('users', views.Users.as_view(), name='users'),
    path('images', views.Images.as_view(), name='images'),
    path('users/register', views.register, name='register'),
    path('users/login', views.login, name='login'),
    path('model/predict', views.predict, name='predict'),
]
