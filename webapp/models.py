from plistlib import UID
from django.db import models
from django.forms import EmailField


class Img(models.Model):
    icreate_date = models.DateTimeField()
    imgdata = models.ImageField()

class User(models.Model):
    ucreate_date = models.DateTimeField()
    email = models.EmailField()
    passwd = models.CharField(max_length=20)
    typems = models.CharField(max_length=20)
    imgs = models.ForeignKey(Img, on_delete=models.CASCADE)