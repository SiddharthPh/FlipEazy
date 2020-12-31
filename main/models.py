from django.db import models
# Create your models here.
class tool(models.Model):
    name=models.CharField(max_length=300, blank=True, null=True)
    email=models.EmailField(max_length=254,null=True)
    url=models.URLField(max_length=200,null=True)
    def __str__(self):
        return self.url

class contactus_form(models.Model):
    name=models.CharField(max_length=300, blank=True, null=True)
    email=models.EmailField(max_length=254,null=True)
    message=models.TextField(max_length=500,null=True)
    def __str__(self):
        return self.name
class newsletter(models.Model):
    email=models.EmailField(max_length=400,null=True)
    def __str__(self):
        return self.email