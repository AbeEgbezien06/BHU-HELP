from rest_framework import serializers
from .models import CategoryComplaint, Complaint




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryComplaint
        fields = ('id', 'name')   



class ComplaintSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Complaint
        fields = ('id',
                  'name',
                  'description',
                  'category',
                  'hostel',
                  'mark_as_done',
                  )
