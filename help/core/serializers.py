from rest_framework import serializers
from .models import CategoryComplaint, Complaint




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryComplaint
        fields = ('name')   



class ComplaintSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    class Meta:
        model = Complaint
        fields = ('name',
                  'description',
                  'category',
                  'hostel',
                  'mark_as_done',
                  )
