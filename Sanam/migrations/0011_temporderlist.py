# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0010_remove_ticket_seatnum'),
    ]

    operations = [
        migrations.CreateModel(
            name='tempOrderlist',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pursuitNum', models.CharField(max_length=14)),
                ('user', models.ForeignKey(to='Sanam.Buyer')),
            ],
        ),
    ]
