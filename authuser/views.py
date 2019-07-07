from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK
)

User = get_user_model()


class LoginApiView(APIView):
    """
    :param - email and password
    :return - Loged User Data and User Token
    """

    def post(self, request, *args, **kwargs):

        username = request.data.get("username", "")
        password = request.data.get("password", "")

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(email=username, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_400_BAD_REQUEST)


        token = None
        if user and user is not None:
            token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, "email": user.email, "useraname": user.email},
                        status=HTTP_200_OK, )


class UserRegisterApiView(generics.CreateAPIView):
    """
    Register User APi
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailApiView(APIView):

    def get_object(self, queryset=None):
        return self.request.user

    def get(self, request, format=None):
        """
        On The Basis of Token return valid user Profile
        :param request: Token(header)*,
        :return: User Related Data
        """

        users = User.objects.filter(id=self.get_object().id)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data[0])