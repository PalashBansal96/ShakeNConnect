# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_handshake'),
    ]

    operations = [
        migrations.AddField(
            model_name='handshake',
            name='u1check',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='handshake',
            name='u2check',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
