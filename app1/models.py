from django.db import models

# Create your models here.


class Details(models.Model):
    cname =models.CharField(max_length=10)
    