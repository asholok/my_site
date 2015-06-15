# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0002_user_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_mail',
            field=models.CharField(unique=True, max_length=40),
            preserve_default=True,
        ),
    ]
