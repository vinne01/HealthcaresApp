from django.db import models
#first import django files when admin panel makethenuser comes
from django.contrib.auth.models import User
# Create your models here.
class Tweet(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE)
#  text=models.TextField(max_length=400)
#  photo=models.ImageField(upload_to='photo/',blank=True,null=True)
 name = models.CharField(max_length=255,default="enter name")
 description = models.TextField(blank=True)  # Allow for optional descriptions
 price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # For monetary values
 created_at=models.DateTimeField(auto_now_add=True)
 updated_at=models.DateTimeField(auto_now=True)
 
 #it help to modify through username 
 def ___str__(self):
     return f'{self.user.username} - {self.text[:10]}'