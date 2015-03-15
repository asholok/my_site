from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    user_mail = models.CharField(max_length=40)
    password = models.CharField(max_length=100)

    def is_authenticated(self):
    	return True
    	
    def __unicode__(self):
        return self.username

# Create your models here.
