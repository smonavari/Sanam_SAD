# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0005_auto_20150803_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='addtime',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='avgrate',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='event',
            name='numofperson',
            field=models.IntegerField(default=0),
        ),
    ]
