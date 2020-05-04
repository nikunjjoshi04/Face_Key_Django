from django.urls import path
from .views import HomePageView, img, video_ajax


app_name = 'detection'

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('img/', img, name='img'),
    path('video_ajax/', video_ajax, name='video_ajax'),
]
