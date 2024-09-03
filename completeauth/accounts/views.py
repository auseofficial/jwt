from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer


class LoginAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                email = serializer.validated_data['email']
                password = serializer.validated_data['password']

                user = authenticate(email=email, password=password)

                if user is None:
                    return Response({
                        'status': 400,
                        'message': 'Invalid Password',
                        'data': {}
                    })

                if user.is_verified is False:
                    return Response({
                        'status': 400,
                        'message': 'Your account is not verified',
                        'data': {}
                    })

                refresh = RefreshToken.for_user(user)

                return Response({
                    'status': 200,
                    'message': 'Login successful',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })

            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal server error',
                'data': {}
            })
