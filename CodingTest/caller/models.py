from django.db import models


class ContactDetail(models.Model):
    user_id=models.IntegerField(unique=False)
    full_name=models.CharField(max_length=100,default='Unknown')
    phone_no=models.CharField(max_length=100)

class SpamDetail(models.Model):
    phone_no=models.CharField(unique=True,max_length=100)
    spam_count=models.IntegerField(default=0)



