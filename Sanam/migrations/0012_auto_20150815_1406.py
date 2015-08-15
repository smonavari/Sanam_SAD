# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0011_temporderlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='tempTicket',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('cap', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='temporderlist',
            name='user',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='orderList',
            field=models.ForeignKey(related_name='order', to='Sanam.OrderList'),
        ),
        migrations.AlterField(
            model_name='tickettype',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='tempOrderlist',
        ),
        migrations.AddField(
            model_name='tempticket',
            name='ticketType',
            field=models.ForeignKey(to='Sanam.TicketType'),
        ),
    ]
