from django.shortcuts import render
from .models import *
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
# Create your views here.


class complaint(APIView):
    def get(self, request, format=None):
        complaint = Complaint.objects.all()
        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data)