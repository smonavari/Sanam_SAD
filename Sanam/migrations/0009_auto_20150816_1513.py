# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0008_auto_20150816_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='make', auto_choose=True, chained_model_field='subcategory', to='Sanam.Category', null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phoneNumber',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
