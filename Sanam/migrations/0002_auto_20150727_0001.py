# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventimage',
            name='event',
            field=models.ForeignKey(related_name='images', to='Sanam.Event'),
        ),
    ]
