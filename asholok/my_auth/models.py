import hashlib
import os
from django.db import models

def get_upload_path(instance, filename):
    return os.path.join('users_avatar', instance.user_mail)

class User(models.Model):
    user_mail = models.CharField(max_length=40, unique=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    images = models.ImageField(upload_to=get_upload_path, blank=True)

    def is_authenticated(self):
        return True
    
    def save(self, *args, **kwargs):
        self.password = hashlib.md5(self.password).hexdigest()

        super(User, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.username

# Create your models here.
