from django.db import models

# Create your models here.

class Complaint(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'complaints'
        ordering = ('date_added',)

    def __str__(self) -> str:
        return self.name
    

    