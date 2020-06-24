from allauth.account.forms import SignupForm, LoginForm
from face_key.constants import *


class CustomSignupForm(SignupForm):

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        os.makedirs(TRAIN_IMAGES_PATH + user.username + '_' + str(user.id))
        return user


class CustomLoginForm(LoginForm):
    pass
