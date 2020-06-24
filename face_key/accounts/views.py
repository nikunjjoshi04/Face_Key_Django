import os
from allauth.account.views import SignupView, LoginView

from face_key.constants import *
from .forms import CustomSignupForm, CustomLoginForm

# Create your views here.


class CustomSignupView(SignupView):
    template_name = 'accounts/signup.html'
    form_class = CustomSignupForm

    def form_valid(self, form):
        return super(CustomSignupView, self).form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = CustomLoginForm

    def form_valid(self, form):
        return super(CustomLoginView, self).form_valid(form)








