from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save, pre_save
from rest_framework.exceptions import ValidationError


class UserManager(BaseUserManager):
    """
    Helps django work with our custom model
    """

    def create_user(self,email,password = None):
        """
        Create new user in a system
        """

        if not email:
            raise ValueError("user must have enter a emial")

        email = self.normalize_email(email)
        user = self.model(email = email)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,password):
        """
        Create a super user
        """

        user = self.create_user(email,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user



class AuthUser(AbstractBaseUser,PermissionsMixin):
    """
    Represent a "user profile" in our project
    """


    email = models.EmailField(max_length = 255, unique=True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


def pre_save_user(sender, instance, *args, **kwargs):
    try:
        old = AuthUser.objects.get(id=instance.id)
    except:
        old = None
    if old is not None:

        user_data = AuthUser.objects.all()
        # Check Email already exist or not
        if old.email != instance.email:
            if (instance.email) in list(user_data.values_list('email', flat=True)):
                raise ValidationError({'name': 'Sorry you cannot change this'})


pre_save.connect(pre_save_user, sender=AuthUser)