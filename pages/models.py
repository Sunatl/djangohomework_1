from django.db import models
from django.contrib.auth.models import User




class Company(models.Model):
    name = models.CharField( max_length=50)
    imeges = models.ImageField(upload_to="static/images",default="ninja.jpg")
    def __str__(self):
        return self.name

class Cars(models.Model):
    name = models.CharField( max_length=50)
    due_date = models.DateField(auto_now=False)
    status = models.CharField( max_length=50)
    imeges = models.ImageField(upload_to="static/images")
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company = models.ForeignKey("Company",on_delete=models.CASCADE)
    def __str__(self):
        return self.name
