# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0008_tickettype_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickettype',
            name='event',
            field=models.ForeignKey(related_name='ticktype', to='Sanam.Event'),
        ),
    ]
