from django.db import models
from django.contrib.auth.models import User
from PIL import Image

THUMBNAIL_MAX_DIMENSION = 500


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_images')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save()
        img = Image.open(self.image.path)
        if any([
            img.height > THUMBNAIL_MAX_DIMENSION,
            img.width > THUMBNAIL_MAX_DIMENSION
        ]):
            img.thumbnail((THUMBNAIL_MAX_DIMENSION, THUMBNAIL_MAX_DIMENSION))
            img.save(self.image.path)



