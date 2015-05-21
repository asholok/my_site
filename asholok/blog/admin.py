from django.contrib import admin
#from django.contrib.auth.models import User as DjUser
from blog.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
#admin.site.register(DjUser)

# Register your models here.
