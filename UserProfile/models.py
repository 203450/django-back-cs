from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class TableProfile(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    url_image = models.ImageField(null=True,blank=True, default='', upload_to='img/')