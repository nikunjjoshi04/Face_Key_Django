from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('custom-signup/', views.CustomSignupView.as_view(), name='account_signup'),
    path('custom-login/', views.CustomLoginView.as_view(), name='account_login'),
]