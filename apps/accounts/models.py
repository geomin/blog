from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    gender = models.CharField(max_length=1, choices=GENDER, default='m')
    user = models.ForeignKey(User)
