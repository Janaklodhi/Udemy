from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .utils import create_jwt_token, decode_jwt_token
from .models import User


class LoginAPIView(APIView):
    def post(self, request):
        """
        Handle user login and return a JWT token.
        """
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token = create_jwt_token(user)
            return Response({
                'status': 'success',
                'message': 'Login successful',
                'token': token,
            }, status=status.HTTP_200_OK)
        return Response({
            'status': 'error',
            'message': 'Invalid credentials',
        }, status=status.HTTP_401_UNAUTHORIZED)


class VerifyTokenAPIView(APIView):
    def post(self, request):
        """
        Verify the provided JWT token.
        """
        token = request.data.get('token')
        payload = decode_jwt_token(token)
        if 'error' in payload:
            return Response({
                'status': 'error',
                'message': payload['error'],
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response({
            'status': 'success',
            'message': 'Token is valid',
            'data': payload,
        }, status=status.HTTP_200_OK)
