# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0015_auto_20150817_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('rate', models.IntegerField()),
                ('event', models.ForeignKey(to='Sanam.Event')),
                ('user', models.ForeignKey(to='Sanam.Member')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together=set([('event', 'user')]),
        ),
    ]
