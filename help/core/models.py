from django.db import models
from django.contrib.auth.models import User

# Create your models here.

<<<<<<< HEAD
class Profile(models.Model):
     user = models.OneToOneField("User.Model", verbose_name=_("User"), on_delete=models.CASCADE)
     room_number = models.CharField(max_length=15, blank=null, null=True)
     phone_number = models.CharField(max_lenght=100, blank=null, null=True)
     hostel = models.ForeignKey('Hostel', on_delete=models.SET_NULL, null=True)

     def __str__(self):
         return self.user.username

=======

class CategoryComplaint(models.Model):
    cat_name = models.CharField(max_length=80)

    def __str__(self):
        return self.cat_name
>>>>>>> 225f72df91d0081e76f67753f95f67a628a2480a
class Complaint(models.Model):
    MY_CHOICES = (
        ('1','Old boys Hostel'),
        ('2','New boys Hostel'),
        ('3', 'Old Girls Hostel'),
        ('4', 'New Girls Hostel')
    )
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    category = models.ForeignKey(CategoryComplaint, related_name="complaints", on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    hostel = models.CharField(max_length=10, choices=MY_CHOICES, blank=True, null= True)
    mark_as_done = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Complaints'
        ordering = ('date_added',)

    def __str__(self) -> str:
        return f"{self.name}, {self.hostel}, {str(self.date_added)}"
    


