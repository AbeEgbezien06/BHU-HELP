from django.db import models
from django.contrib.auth.models import User

# Create your models here.





class CategoryComplaint(models.Model):
    cat_name = models.CharField(max_length=80)

    def __str__(self):
        return self.cat_name
class Complaint(models.Model):

    MY_CHOICES =(
                  ('1', 'old boys hostel'),
                  ('2', 'new boys hostel'),
                  ('3', 'old girls hostel'),
                  ('4', 'new girls hostel 1'),
                  ('5', 'new girls hostel 2'),
    )
                  
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    category = models.ForeignKey(CategoryComplaint, related_name="complaints", on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    hostel = models.CharField(max_length=10, choices=MY_CHOICES, blank=True, null= True)
    mark_as_done = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'complaints'
        ordering = ('date_added',)

    def __str__(self) -> str:
        return self.name
    

    