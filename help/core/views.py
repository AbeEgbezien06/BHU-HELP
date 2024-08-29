from django.shortcuts import render
from .models import *
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import viewsets
from .forms import ComplaintForm
# Create your views here.


class complaint(APIView):
    def get(self, request, format=None):
        complaints = Complaint.objects.all()
        serializers = ComplaintSerializer(complaints, many=True).data
        return render(request, 'index.html', {
            'complaints_json':serializers
        })
    



class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

class ComplaintDetail(APIView):
    def get_object(self, category_slug, complaint_slug):
        try:
            return Complaint.objects.filter(category__slug=category_slug).get(slug=complaint_slug)
        except Complaint.DoesNotExist:
            raise Http404
        
    def get(self, request, category_slug, complaint_slug, format=None):
        complaint = self.get_object(category_slug, complaint_slug)
        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data)
    


class  CategoryDetail(APIView):
    def get_oblect(self, category_slug):
        try:
            return CategoryComplaint.objects.get(slug=category_slug)
        except CategoryComplaint.DoesNotExist:
            raise Http404
        
    def get(self, request, category_slug):
        category = self.get_oblect(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
@api_view(['POST'],)
def newItemForm(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid:
            item  = form.save(commit=False)
            item.save()
        else:
            form = ComplaintForm()
    return render(request, 'newissue.html', {
        'form':form
    })