from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = 'Base Model'
        verbose_name_plural = 'Base Model'


class SubEmail(BaseModel):
    email = models.EmailField(max_length=100, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Sub Email'
        verbose_name_plural = 'Sub Emails'

    def __str__(self):
        return f'{self.email}'
