# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0004_auto_20150801_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventimage',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='EventImage',
            field=models.ImageField(null=True, upload_to='events'),
        ),
        migrations.AddField(
            model_name='event',
            name='dscp',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='EventImage',
        ),
    ]
