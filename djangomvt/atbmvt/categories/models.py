from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = ResizedImageField(
        size=[600, 600],
        crop=['middle', 'center'],
        quality=85,
        force_format='WEBP',
        upload_to='categories/image/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name