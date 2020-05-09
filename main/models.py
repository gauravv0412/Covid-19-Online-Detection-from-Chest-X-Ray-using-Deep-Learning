from django.db import models

# Create your models here.
class Xray(models.Model):
    scan = models.ImageField(upload_to = 'images/')