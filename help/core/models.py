from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.





class CategoryComplaint(models.Model):
    cat_name = models.CharField(max_length=80)
    cat_desc = models.TextField(max_length=255, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.cat_name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    



class Complaint(models.Model):

    MY_CHOICES = (
    ('old boys hostel', 'OBH'),
    ('new boys hostel', 'NBH'),
    ('old girls hostel', 'OGH'),
    ('new girls hostel 1', 'NGH1'),
    ('new girls hostel 2', 'NGH2'),
    )
    
    BLOCK_CHOICES = (
        ('enoch', 'Block A'),
        ('Daniel', 'Block B'),
        ('moses', 'Block C'),
    )


                  
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    category = models.ForeignKey(CategoryComplaint, related_name="complaints", on_delete=models.CASCADE, blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)
    hostel = models.CharField(max_length=50, choices=MY_CHOICES, blank=True, null= True)
    block = models.CharField(max_length=50, choices=BLOCK_CHOICES, blank=True, null=True)
    mark_as_done = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'complaints'
        ordering = ('-date_added',)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # Assuming 'category' is a ForeignKey or CharField in your model
            # if self.category:
                # self.slug = slugify(f"{self.category}-{self.name}")           
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    

    