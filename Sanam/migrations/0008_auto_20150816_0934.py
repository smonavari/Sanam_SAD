# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0007_auto_20150804_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickettype',
            name='event',
            field=models.ForeignKey(to='Sanam.Event', related_name='Tickets'),
        ),
    ]
