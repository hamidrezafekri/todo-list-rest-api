from multiprocessing.managers import BaseManager

from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, firstname, lastname, phone_number, password, **extra_fields):
        if not firstname:
            raise ValueError(_('firstname is required'))
        if not lastname:
            raise ValueError(_('lastname is required'))
        if not phone_number:
            raise ValueError(_('phone_number is required'))
        user = self.model(phone_number=phone_number, firstname=firstname, lastname=lastname, **extra_fields)
        if not password:
            raise ValueError(_('password is required'))
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self  ,firstname , lastname , phone_number , password , **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(firstname, lastname, phone_number, password, **extra_fields)



class User(models.Model):
    firstname = models.CharField(max_length=100 , verbose_name="user's firstname")
    lastname = models.CharField(max_length=100 , verbose_name="user's lastname")
    phone_number = models.CharField(max_length=13 , verbose_name="user's phone_number")
    password = models.CharField(max_length=64  , verbose_name="user's password")



    username = None
    USERNAME_FIELD  = 'phone_number'
    REQUIRED_FIELEDS = ['firstname' , 'lastname' , 'password']

    objects = UserManager()


