from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.utils import *
from accounts.serializers import *


class SignUp(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            user_data = CustomUserSerializer(user, context={'request':request}).data
            print(user_data)
            return Response({"user": user_data, **token}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInfo(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user
        user_data = {
            "id": user.id,
            "email": user.email,
            "display_name": user.display_name,
        }
        return Response({"user": user_data}, status=status.HTTP_200_OK)


class LogOut(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response({"detail": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklist the token to log out the user

            return Response({"message": "User logged out successfully."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class SignIn(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSignInSerializer(data=data)
            if serializer.is_valid():
                user = serializer.validated_data["user"]
                token = get_tokens_for_user(user)
                user_data = CustomUserSerializer(user, context={'request':request}).data
                return Response({"user": user_data, **token}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {
                        "error": "Invalid login credentials",
                        "details": serializer.errors,
                    },
                    status=400,
                )
        except Exception as e:
            return Response(str(e))
