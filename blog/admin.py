from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)    # register the model, to make model visible on the admin page
admin.site.register(Comment)