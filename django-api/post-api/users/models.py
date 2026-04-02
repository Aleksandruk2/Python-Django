from django.db import models
from django.contrib.auth.models import AbstractUser

# це кастомна модель користувача, яка замінює стандартну модель користувача django і дозволяє додавати власні поля та змінювати поведінку.
class CustomUser(AbstractUser):
    image_small = models.ImageField(upload_to='images/', blank=True, null=True)
    image_medium = models.ImageField(upload_to='images/', blank=True, null=True)
    image_large = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.email