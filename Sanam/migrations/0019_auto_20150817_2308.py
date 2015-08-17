# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0018_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='tempTicket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('cap', models.IntegerField(default=0)),
                ('ticketType', models.ForeignKey(to='Sanam.TicketType', related_name='order')),
            ],
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='seatNum',
        ),
        migrations.AddField(
            model_name='ticket',
            name='cap',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='orderList',
            field=models.ForeignKey(to='Sanam.OrderList', related_name='orderlisttick'),
        ),
    ]
