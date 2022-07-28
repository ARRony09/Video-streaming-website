from django.urls import path
from . import views
from .views import VideoListView

app_name='App_stream'

urlpatterns = [
    path('',VideoListView.as_view(),name='home'),
    path('details/<pk>',views.video_details_comment,name='details'),
    path('add/',views.addvideo,name='add')
]
