from multiprocessing.managers import BaseManager

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, first_name, last_name, phone_number, password, **extra_fields):
        if not first_name:
            raise ValueError(_('first_name is required'))
        if not last_name:
            raise ValueError(_('last_name is required'))
        if not phone_number:
            raise ValueError(_('phone_number is required'))
        user = self.model(phone_number=phone_number, first_name=first_name, last_name=last_name, **extra_fields)
        if not password:
            raise ValueError(_('password is required'))
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self  ,first_name , last_name , phone_number , password , **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(first_name, last_name, phone_number, password, **extra_fields)


#TODO: add validation for fields and add image filed too with minIo
class Profile(AbstractUser):
    first_name = models.CharField(max_length=100 , verbose_name="user's firstname")
    last_name = models.CharField(max_length=100 , verbose_name="user's lastname")
    phone_number = models.CharField(max_length=13 , verbose_name="user's phone_number" , unique=True)
    password = models.CharField(max_length=128  , verbose_name="user's password")



    username = None
    USERNAME_FIELD  = 'phone_number'
    REQUIRED_FIELDS = ['first_name' , 'last_name' , 'password']

    objects = UserManager()


