from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class accounts(models.Model):
    user = models.OneToOneField(User)
    mobile_no = models.CharField(max_length=20, default=None,blank=True)
    date_of_birth = models.DateField(default=timezone.now)
    gender_choice = (
        ('M', 'Male'), ('F', 'Female')
    )
    gender = models.CharField(max_length=10, choices=gender_choice)

    @python_2_unicode_compatible
    def __str__(self):
        return self.first_name
