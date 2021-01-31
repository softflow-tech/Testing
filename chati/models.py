from django.db import models
from django.contrib.auth import get_user_model

# from django.contrib.auth.models import AbstractUser, BaseUserManager ## A new class is imported. ##
# from django.db import models
# from django.utils.translation import ugettext_lazy as _


# class UserManager(BaseUserManager):
#     """Define a model manager for User model with no username field."""

#     use_in_migrations = True

#     def _create_user(self, email, password, **extra_fields):
#         """Create and save a User with the given email and password."""
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         """Create and save a regular User with the given email and password."""
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         """Create and save a SuperUser with the given email and password."""
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(email, password, **extra_fields)

# class User(AbstractUser):
#     """User model."""

#     username = None
#     USERNAME_FIELD = 'email'
#     email = models.EmailField(_('email address'), unique=True)
#     first_name = models.CharField(_('first name'), max_length=64)
#     last_name = models.CharField(_('last name'),max_length=64)

#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email

class Userdetail(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    friends_ids = models.ManyToManyField('self',blank=True)

    def __str__(self):
        return str(self.user_id)

class Group(models.Model):
    groupname = models.CharField(max_length=128)
    members_ids = models.ManyToManyField(get_user_model(), through='Membership')

    def __str__(self):
        return self.groupname

class Membership(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    group_member_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
