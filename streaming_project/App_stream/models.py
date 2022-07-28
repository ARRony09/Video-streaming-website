from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    video=EmbedVideoField()
    desc=models.TextField(default="")
    created=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=('-created',)
    def __str__(self):
        return self.title


class UserComment(models.Model):
    video_post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='video_comment')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    comment=models.TextField()
    comment_date=models.DateTimeField(auto_now_add=True)
