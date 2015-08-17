# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0019_auto_20150817_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickettype',
            name='soldnum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tickettype',
            name='title',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='user',
            field=models.ForeignKey(to='Sanam.Buyer', related_name='buyer'),
        ),
        migrations.AlterField(
            model_name='tickettype',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tickettype',
            name='event',
            field=models.ForeignKey(to='Sanam.Event', related_name='ticktype'),
        ),
    ]
