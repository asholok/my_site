from django.db import models
from slugify import slugify
from my_auth.models import User
import os


def get_upload_path(instance, filename):
    return os.path.join(
        instance.author.user_mail, '{}_{}'.format(instance.slug, filename))

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True)
    short_body = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User)
    image = models.ImageField(upload_to=get_upload_path, blank=True)
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        sample_slug = slugify(self.title)
        #match_check = Post.object.filter(slug=sample_slug).exists()
            
        if Post.objects.filter(slug=sample_slug).exists():
            self.slug = '{}_{}'.format(self.date, sample_slug)
        else:
            self.slug = sample_slug

        super(Post, self).save(*args, **kwargs)
        
