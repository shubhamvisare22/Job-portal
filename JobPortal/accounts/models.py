from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('company', 'Company'),
        ('candidate', 'Candidate'),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=USER_ROLES, default='candidate')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_users', verbose_name='groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_users', verbose_name='user permissions')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
