from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# each model maps to a single db table
# the name of this post table in the db is blog_post


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # the author who is a user can have
    # many posts but a post cannot have many authors hence a one to many field

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.id})
