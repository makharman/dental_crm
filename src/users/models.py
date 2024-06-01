from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from .managers import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    mobile_phone = models.CharField(max_length=15, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Уникальный related_name
        blank=True,
        help_text='Группы, к которым принадлежит этот пользователь. Пользователь получит все разрешения, предоставленные каждой из его групп.',
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Уникальный related_name
        blank=True,
        help_text='Конкретные разрешения для этого пользователя.',
        related_query_name='custom_user'
    )
    
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'UserAccount'
        ordering = ['-created_at']
        verbose_name = 'UserAccount'
        verbose_name_plural = 'UserAccounts'

    def __str__(self) -> str:
        return f'{self.id} - {self.email}'

    
