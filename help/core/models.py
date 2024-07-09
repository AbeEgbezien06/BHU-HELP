from django.db import models
from django.contrib.auth.models import User

# Create your models here.

<<<<<<< HEAD
class Profile(models.Model):
     user = models.OneToOneField("User", verbose_name=_("User"), on_delete=models.CASCADE)
     room_number = models.CharField(max_length=15, blank=True, null=True)
     phone_number = models.CharField(max_lenght=20, blank=True, null=True)
     email = models.EmailField(max_length=100, blank=True, null=True)
     hostel = models.ForeignKey('Hostel', on_delete=models.SET_NULL, null=True)

     def __str__(self):
         return self.user.username

=======


class CategoryComplaint(models.Model):
    cat_name = models.CharField(max_length=80)

    def __str__(self):
        return self.cat_name
>>>>>>> 1874b081e1381fe943dbb56bd6a46d380cceedea
class Complaint(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'complaints'
        ordering = ('date_added',)

    def __str__(self) -> str:
        return self.name
    

    