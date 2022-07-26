from . import views
from django.contrib import admin
from django.urls import path,include


app_name='App_login'

urlpatterns = [
    path('signup/',views.signup_user,name='signup'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('search/',views.search,name='search'),
]
