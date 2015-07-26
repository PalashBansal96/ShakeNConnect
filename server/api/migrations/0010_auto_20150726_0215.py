# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20150725_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='facebook',
            field=models.CharField(max_length=70, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pin',
            name='git',
            field=models.CharField(max_length=70, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pin',
            name='linkedin',
            field=models.CharField(max_length=70, blank=True),
            preserve_default=True,
        ),
    ]
