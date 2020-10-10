from django.db import models


# Create your models here.
class Resume(models.Model):
    Email = models.CharField(max_length=120)
    Password = models.CharField(max_length=25)
    Full_Name = models.CharField(max_length=120)
    DOB = models.CharField(max_length=120)
    Last_Degree = models.CharField(max_length=120)
    Profile_Picture = models.ImageField(default=None, upload_to="images")
    user = models.CharField(max_length=120)
