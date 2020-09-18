from django.db import models
# Create your models here.
class tool(models.Model):
    name=models.CharField(max_length=300, blank=True, null=True)
    email=models.EmailField(max_length=254,null=True)
    url=models.URLField(max_length=200,null=True)

   