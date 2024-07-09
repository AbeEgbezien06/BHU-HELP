from django.shortcuts import render, redirect
from .models import *
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import *
from .forms import SignupForm
# Create your views here.


class complaint(APIView):
    def get(self, request, format=None):
        complaint = Complaint.objects.all()
        serializer = ComplaintSerializer(complaint, many=True)
        return render(request, 'core/index.html', {"complaints":serializer.data})
    

@api_view
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm
    return render(request, 'core/login.html', {
        'form':form
    })
