from django.db import models

# Create your models here.
class image(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image = models.FileField(upload_to='document/')
    up_loadeat = models.DateTimeField(auto_now_add = True)

class image_desc(models.Model):
    datetime = models.DateTimeField()
