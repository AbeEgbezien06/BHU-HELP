from rest_framework import serializers
from .models import CategoryComplaint, Complaint


class ComplaintSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(many=True)
    class Meta:
        model = Complaint
        fields = (
            'id',
            'name',
            'description',
            'date_added',
            'category',
            'hostel',
            'block',
            'mark_as_done',
            'get_absolute_url',
        )


class CategorySerializer(serializers.ModelSerializer):
    complaint = ComplaintSerializer(many=True)
    class Meta:
        model = CategoryComplaint
        fields = (
            'id',
            'cat_name',
            'cat_desc',
            'get_absolute_url',
        )  