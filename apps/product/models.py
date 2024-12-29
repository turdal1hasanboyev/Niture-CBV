from django.db import models

import uuid
from ckeditor.fields import RichTextField

from django.utils.text import slugify
from django.urls import reverse

from django.core.validators import MinValueValidator, MaxValueValidator

from apps.user.models import CustomUser
from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    image = models.ImageField(upload_to='category_images', default='images/default-image.png')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.name}"
    

class Banner(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='banner/', default='images/default-image.png')

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return f"{self.name}"
    

class Product(BaseModel):
    name = models.CharField(max_length=250, unique=True, db_index=True)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=250, db_index=True)
    image = models.ImageField(upload_to="product_images/", default='images/default-image.png')
    description = RichTextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    percentage = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='product_category')
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):  
        if not self.slug and self.name:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    @property
    def discount(self):
        if self.percentage:
            return self.price - (self.price * self.percentage) / 100
        return self.price
    
    @property
    def reviews_count(self):
        return self.rates.count()


class Review(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rates')
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    message = RichTextField(null=True, blank=True)
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.product}"
    