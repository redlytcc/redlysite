from django.db import models
import re
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin,UserManager)
from django.contrib.auth.models import AbstractUser

class User(AbstractBaseUser):
    username=models.CharField('Apelido',max_length=40,unique=True,validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),'o nome do usuario so pode conter letras digitos ou os''seguintes caraters:@/./+/-/_','invalid')])
    email=models.EmailField('E-mail',unique=True)
    name=models.CharField('Nome',max_length=40)
    is_active=models.BooleanField('Esta ativo?',blank=True,default=True)
    is_staff=models.BooleanField('equipe',blank=True,default=False)
    date_joined=models.DateTimeField('Data de Criacao',auto_now_add=True)

    objects=UserManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email','name']

    def __str__(self):
        return self.name or self.username
    def get_short_name(self):
        return self.username
    def get_full_name(self):
        return str(self)
    class Meta:
        verbose_name='usuario'
        verbose_name_plural='usuarios'
