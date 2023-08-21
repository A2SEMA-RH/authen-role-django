from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_etudiant = models.BooleanField('Is etudiant', default=False)
    is_enseigant = models.BooleanField('Is enseignat', default=False)

