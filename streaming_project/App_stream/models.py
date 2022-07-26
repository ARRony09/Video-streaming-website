from pyexpat import model
from turtle import title
from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    video=EmbedVideoField()
    desc=models.TextField(default="")

    def __str__(self):
        return self.title