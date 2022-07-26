from django.urls import path,include
from . import views
from .views import VideoDetailView, VideoListView

app_name='App_stream'

urlpatterns = [
    path('',VideoListView.as_view(),name='home'),
    path('details/<pk>',VideoDetailView.as_view(),name='details'),
]
