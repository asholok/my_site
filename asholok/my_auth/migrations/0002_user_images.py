# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import my_auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='images',
            field=models.ImageField(upload_to=my_auth.models.get_upload_path, blank=True),
            preserve_default=True,
        ),
    ]
