from django.db import models
from django.contrib.auth.models import AbstractUser

# class myUser(AbstractUser):
#     church_group = models.CharField(max_length = 200)

class myUser(models.Model):
    name = models.CharField(max_length=10)
    # group = models.CharField(max_length=10)
    birthday = models.CharField(max_length=20,blank=True,null=True,default='정보없음')
    phone = models.CharField(max_length=13,blank=True, null=True,default='정보없음')
    age = models.IntegerField()

    def __str__(self):
        return self.name 

class myPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    enddate = models.DateField(blank=True,null=True)
    writtendate = models.DateField(auto_now_add=True)

    def __str__(self): 
        return self.title
