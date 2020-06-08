from django.db import models
from django.contrib.auth.models import AbstractUser



# Custom User Model to store mobile number and overwrite first_name and last_name of user model to be required.
class CustomUser(AbstractUser):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.first_name+self.last_name

