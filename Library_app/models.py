
from django.db import models

from multiprocessing.spawn import import_main_path
from operator import mod
from tabnanny import verbose

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class BookModel(models.Model):
    book_name = models.CharField(max_length=100)
    book_price = models.FloatField()
    book_pages = models.IntegerField()
    book_author = models.CharField(max_length=100)
    book_publisher = models.CharField(max_length=100)


    def __str__(self):
        return self.book_name





# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
        if not email:
            raise ValueError('Email must be provided')
        if not password:
            raise ValueError('Password is not Provided')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, last_name, mobile, password, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile = models.CharField(max_length=254)
    address = models.CharField(max_length=254)

    email = models.EmailField(db_index=True, max_length=254, unique=True)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'