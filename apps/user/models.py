from django.db import models

from datetime import date

from ckeditor.fields import RichTextField

from ..common.models import BaseModel
from .managers import CustomUserManager

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser, BaseModel):
    GENDER = (
        ('Ayol', ('Ayol')),
        ('Erkak', ('Erkak')),
    )
    email = models.EmailField(max_length=150, unique=True, db_index=True)
    image = models.ImageField(upload_to='user-images/', default='images/default-user.png', null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, db_index=True, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone_number", "first_name", 'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        if self.username:
            return f'{self.username}'
        if self.get_full_name():
            return f'{self.get_full_name()}'
        return f'{self.email}'
    
    def get_age(self):
        if not isinstance(self.birthday, date):
            return None
        today = date.today()
        age = today.year - self.birthday.year
        if (today.month, today.day) < (self.birthday.month, self.birthday.day):
            age -= 1
        return age
