from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

class StartButton(APIView):
    def post(self, request):
        ...