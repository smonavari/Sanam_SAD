# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0014_auto_20150816_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickettype',
            name='soldnum',
            field=models.IntegerField(default=0),
        ),
    ]
