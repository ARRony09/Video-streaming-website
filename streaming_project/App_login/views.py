from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .forms import UserSignUp
from App_stream.models import Post
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def signup_user(request):
    form=UserSignUp()
    if request.method=='POST':
        form=UserSignUp(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_login:login'))#HttpResponseRedirect(reverse(''))
    return render(request,'App_login/signup.html',context={'form':form})


def login_user(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('App_stream:home')) #HttpResponse("Successful")

    return render(request,'App_login/login.html',context={'form':form})


def logout_user(request):
    logout(request)
    return HttpResponse("Logout successful")


def search(request):
    query=request.GET['query']
    search_title=Post.objects.filter(title__icontains=query)
    return render(request,'App_login/search.html',context={'search_title':search_title})
