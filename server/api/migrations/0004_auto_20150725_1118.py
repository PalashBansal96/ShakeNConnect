# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_shake'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shake',
            name='fingerprint',
            field=models.ForeignKey(to='api.Pin'),
            preserve_default=True,
        ),
    ]
