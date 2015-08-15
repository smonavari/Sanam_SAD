# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0002_auto_20150727_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='seller',
            field=models.ForeignKey(to='Sanam.EventMaker', null=True),
        ),
    ]
