from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):
        """ Creates and saves a new user """
        if not username:
            raise ValueError(_("Username is required"))

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """ Creates and saves a new super user """
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser, PermissionsMixin):
    """ Custom user model that supports using email instead of username """
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=2555, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    image = models.ImageField(default='profiles/default.jpg', upload_to='profiles')
    bio = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    username = username
    USERNAME_FIELD = 'username'
    search_fields = ['email', 'name', 'username']

    def __str__(self):
        return f"{self.name} <{self.email}>"
