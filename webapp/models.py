from plistlib import UID
from django.db import models
from django.forms import EmailField


class Img(models.Model):
    create_date = models.DateTimeField()
    imgdata = models.ImageField()
    imgnum = models.CharField(max_length=20)

class User(models.Model):
    email = models.EmailField()
    passwd = models.CharField(max_length=20)
    uqid = models.CharField(max_length=20)
    typems = models.CharField(max_length=20)
    imgs = models.ForeignKey(Img, on_delete=models.CASCADE)