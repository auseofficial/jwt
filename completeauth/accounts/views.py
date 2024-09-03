from django.shortcuts import render

class LoginAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer= LoginSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data['email']
                password = serializer.data['passowrd']
                
            return Response({
                'status': 400,
                'message':'Something Went Wrong',
                'data':serializer.errors
            })
