from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

User = get_user_model()


class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': CustomUserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class TokenRefreshView(APIView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh')
        if refresh_token:
            try:
                refresh = RefreshToken(refresh_token)
                access_token = str(refresh.access_token)
                return Response({'access': access_token})
            except TokenError as e:
                return Response({'error': 'Invalid or expired refresh token'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Refresh token not provided'}, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutAPIView(APIView):
    def post(self, request):
        return Response({"detail": "User logged out"}, status=status.HTTP_204_NO_CONTENT)
