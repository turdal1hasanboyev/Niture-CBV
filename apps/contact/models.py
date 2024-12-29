from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Contact(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=15)
    message = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f"{self.name}"
    