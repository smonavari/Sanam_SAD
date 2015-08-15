# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0009_auto_20150811_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='seatNum',
        ),
    ]
