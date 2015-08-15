# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0012_auto_20150815_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempticket',
            name='ticketType',
            field=models.ForeignKey(to='Sanam.TicketType', related_name='order'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='orderList',
            field=models.ForeignKey(to='Sanam.OrderList'),
        ),
    ]
