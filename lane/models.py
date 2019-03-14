from django.db import models

# Create your models here.
class image(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image = models.FileField(upload_to='document/')
    up_loadeat = models.DateTimeField(auto_now_add = True)

class image_desc(models.Model):
    datetime = models.DateTimeField()
    # image = models.FileField(upload_to='images/')
    # name = models.CharField(max_length=50, blank=True)
    # up_loadedat = models.DateTimeField(auto_now_add = True)


# class image_metadata(models.Model):
#     datetime = models.DateTimeField()
#     image = models.FileField(upload_to='images/')
#     name = models.CharField(max_length=50, blank=True)
#     up_loadedat = models.DateTimeField(auto_now_add = True)
