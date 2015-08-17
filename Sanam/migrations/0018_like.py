# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0017_remove_comment_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('comment', models.ForeignKey(to='Sanam.Comment')),
                ('user', models.ForeignKey(to='Sanam.Member')),
            ],
        ),
    ]
