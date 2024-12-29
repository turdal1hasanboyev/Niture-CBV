from django.db import models

from apps.common.models import BaseModel


class About(BaseModel):
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='about_images/', default='images/default-image.png')

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return f"{self.id}-{self.image}"
