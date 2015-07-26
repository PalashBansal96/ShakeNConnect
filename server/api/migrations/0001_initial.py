# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fingerprint', models.TextField()),
                ('name', models.CharField(max_length=100, blank=True)),
                ('email', models.CharField(max_length=100, blank=True)),
                ('number', models.CharField(max_length=20, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
