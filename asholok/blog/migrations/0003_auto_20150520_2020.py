# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 5, 20, 20, 20, 24, 230284), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.TimeField(default=datetime.datetime(2015, 5, 20, 20, 20, 24, 230311), auto_now_add=True),
            preserve_default=True,
        ),
    ]
