from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class CategoryComplaint(models.Model):
    cat_name = models.CharField(max_length=80)

    def __str__(self):
        return self.cat_name
class Complaint(models.Model):
    MY_CHOICES = (
        ('1','Old boys Hostel'),
        ('2','New boys Hostel'),
        ('3', 'Old Girls Hostel'),
        ('4', 'New Girls Hostel')
    )
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    category = models.ForeignKey(CategoryComplaint, related_name="complaints", on_delete=models.CASCADE, blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)
    hostel = models.CharField(max_length=10, choices=MY_CHOICES, blank=True, null= True)
    mark_as_done = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Complaints'
        ordering = ('date_added',)

    def __str__(self) -> str:
        return f"{self.name}, {self.hostel}, {str(self.date_added)}"
    


