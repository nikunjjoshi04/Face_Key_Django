from django.contrib import admin

from .models import *
from detection.models import UserDates

# Register your models here.


class UserDatesInline(admin.TabularInline):
    model = UserDates
    fk_name = 'user'
    can_delete = True
    extra = 0
    verbose_name_plural = 'Attended Dates'


class CustomUserAdmin(admin.ModelAdmin):
    inlines = [UserDatesInline]


admin.site.register(CustomUser, CustomUserAdmin)