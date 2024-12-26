from django.contrib.auth.models import UserManager

import re


class CustomUserManager(UserManager):
    def create_user(self, username, email, phone_number, first_name, last_name, image=None, description=None, birthday=None, gender=None, password=None, **extra_fields):
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an email address')
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise ValueError('Users must have a valid email address')
        if not phone_number:
            raise ValueError('Users must have a phone number')
        if not re.match(r'^\+?[0-9]{10,15}$', phone_number):
            raise ValueError('Users must have a valid phone number')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, phone_number=phone_number, first_name=first_name, last_name=last_name, image=image, description=description, birthday=birthday, gender=gender, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, phone_number, first_name, last_name, image=None, description=None, birthday=None, gender=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if not username:
            raise ValueError('Superuser must have an username')
        if not email:
            raise ValueError('Superuser must have an email address')
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise ValueError('Super Users must have a valid email address')
        if not phone_number:
            raise ValueError('Superuser must have a phone number')
        if not re.match(r'^\+?[0-9]{10,15}$', phone_number):
            raise ValueError('Superuser must have a valid phone number')
        if not first_name:
            raise ValueError('Superuser must have a first name')
        if not last_name:
            raise ValueError('Superuser must have a last name')
        
        user = self.create_user(username, email, phone_number, first_name, last_name, image, description, birthday, gender, password, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user
    