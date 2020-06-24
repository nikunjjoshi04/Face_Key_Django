from django.db import models

from accounts.models import CustomUser
# Create your models here.


class UserDates(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    date = models.DateField()
    attend = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {} - {}'.format(self.user, self.date, self.attend)