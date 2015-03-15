# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=150)),
                ('short_body', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to=blog.models.get_upload_path, blank=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(to='my_auth.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
