# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0016_auto_20150817_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='rate',
        ),
    ]
