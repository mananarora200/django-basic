from django.db import models

# Create your models here.
class Image_Model(models.Model):
    tags=models.CharField(max_length=255)
    upload_image=models.ImageField(upload_to='images',blank=True)
