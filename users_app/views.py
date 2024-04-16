from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from users_app.models import User

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        name = request.data.get('name')

        try:
            new_user = User.objects.create(user_id=user_id, name=name)
            new_user.save()
            return Response({"status": "success"}, status=HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"status": f"error: {e}"}, status=HTTP_400_BAD_REQUEST)