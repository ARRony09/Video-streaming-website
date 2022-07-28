from django.db import models
from .models import UserComment,Post
from django import forms


class AddVideoForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','video','desc',)


class UserCommentForm(forms.ModelForm):
    class Meta:
        model=UserComment
        fields=('comment',)