# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0013_auto_20150815_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='cap',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='user',
            field=models.ForeignKey(to='Sanam.Buyer', related_name='buyer'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='orderList',
            field=models.ForeignKey(to='Sanam.OrderList', related_name='orderlisttick'),
        ),
    ]
