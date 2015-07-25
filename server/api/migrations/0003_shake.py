# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150725_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fingerprint', models.TextField()),
                ('lat', models.TextField()),
                ('lon', models.TextField()),
                ('timestamp', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
