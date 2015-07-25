# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20150725_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Handshake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.TextField()),
                ('lon', models.TextField()),
                ('address', models.TextField()),
                ('timestamp', models.TextField()),
                ('user1', models.ForeignKey(related_name='one', to='api.Pin')),
                ('user2', models.ForeignKey(related_name='two', to='api.Pin')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
