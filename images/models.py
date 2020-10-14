from django.db import models

# Create your models here.
class Images (model.Model):
    title = models.CharField(max_length=30)
    description= models.CharField (max_length=30)