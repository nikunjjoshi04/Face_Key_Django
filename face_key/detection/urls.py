from django.urls import path
from .views import HomePageView, img


app_name = 'detection'

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('img/', img, name='img'),
]
