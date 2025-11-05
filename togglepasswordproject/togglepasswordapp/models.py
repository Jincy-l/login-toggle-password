from django.db import models

# Create your models here.
class Login(models.Model):
   email = models.EmailField(unique=True)
   password = models.CharField(max_length=128)
   

class Register(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    address = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.name
