from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    # image = ResizedImageField(
    #     size=[600, 600],
    #     crop=['middle', 'center'],
    #     quality=85,
    #     force_format='WEBP',
    #     upload_to=upload_image,
    #     null=True,
    #     blank=True,
    # )
    image = models.ImageField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.name
