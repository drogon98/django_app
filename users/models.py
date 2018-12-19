from django.db import models
from django.contrib.auth.models import User

from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="defaultimg.jpg", upload_to="profile_img")

    def __str__(self):
        return f"{ self.user.username } Profile"

    def save(self, *args, **kwargs):  # overriding the save method of the model
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            resized_img = (300, 300)
            img.thumbnail(resized_img)
            img.save(self.image.path)
