from django.contrib import admin

from .models import Post

admin.site.site_header="Blog Administration"
admin.site.register(Post)
