# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20150725_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shake',
            name='timestamp',
            field=models.TextField(),
        ),
    ]
