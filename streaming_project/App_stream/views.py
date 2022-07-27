from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView,DetailView
from requests import request
from .models import Post, UserComment
from .forms import UserCommentForm
# Create your views here.

"""def home(request):
    return render(request,'App_stream/home.html',context={})
"""
class VideoListView(ListView):
    model=Post
    template_name='App_stream/home.html'

"""class VideoDetailView(DetailView):
    comment_form=UserCommentForm()
    if request.method=='POST':
        comment_form=UserCommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.user=request.user
    model=Post
    template_name='App_stream/details.html'
    extra_context={'comment_form':comment_form}

"""


def video_details_comment(request,pk):
    post=Post.objects.get(pk=pk)
    #user_comments=UserComment.objects.all()
    #print(user_comments)
    form=UserCommentForm()
    if request.method=='POST':
        comment_form=UserCommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.user=request.user
            comment.video_post=post
            comment.save()
            return HttpResponseRedirect(reverse("App_stream:details",kwargs={'pk':pk}))
    return render(request,'App_stream/details.html',context={'post':post,'form':form})
