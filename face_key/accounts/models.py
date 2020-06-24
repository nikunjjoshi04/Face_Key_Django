from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    @classmethod
    def get(cls, id):
        return cls.objects.get(id=id)
