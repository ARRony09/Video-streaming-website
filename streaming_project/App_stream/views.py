from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.

"""def home(request):
    return render(request,'App_stream/home.html',context={})
"""
class VideoListView(ListView):
    model=Post
    template_name='App_stream/home.html'

class VideoDetailView(DetailView):
    model=Post
    template_name='App_stream/details.html'