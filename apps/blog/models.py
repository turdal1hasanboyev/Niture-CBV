from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Blog(BaseModel):
    name = models.CharField(max_length=250, unique=True, db_index=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='blogs/', default='images/default-image.png')

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return f"{self.name}"
    