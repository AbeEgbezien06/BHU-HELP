from django import forms

from .models import Complaint

CLASSES = 'w-full py-4 px-6 rounded-xl border mb-2'

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = (
            'name',
            'description',
            'category',
            'hostel',
            'block',
        )

    widgets = {
            'category':forms.Select(attrs={
                'class':CLASSES
            }),
            'name':forms.TextInput(attrs={
                'class':CLASSES
            }),
            'description':forms.Textarea(attrs={
                'class':CLASSES
            }),
            'hostel':forms.Select(attrs={
                'class':CLASSES
            }),
            'block':forms.Select(attrs={
                'class':CLASSES
            }),
        }