from django.db import models

# Create your models here.
from django.contrib.auth.models import User, UserManager
from public.models import SEX_CHOICE, STAT_DICT

# user information
class UserInfo(User):
    phoneNum = models.CharField(max_length=15)
    sex = models.CharField(max_length=1, choices=SEX_CHOICE, default='M')
    ages = models.CharField(max_length=3, blank=True)
    headImg = models.URLField(max_length=100, blank=True)
    stat = models.CharField(max_length=5, choices=STAT_DICT, default='S0A')

    def __unicode__(self):
        return self.username

    objects = UserManager()