from rest_framework.views import APIView
from rest_framework.response import Response

class LoginAPI(APIView):
    def post(self, request):
        return Response({'message': 'Login successful'})
