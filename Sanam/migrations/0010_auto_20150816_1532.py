# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0009_auto_20150816_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=smart_selects.db_fields.ChainedForeignKey(null=True, to='Sanam.Category', auto_choose=True, chained_model_field='Subcategory', chained_field='subcategory'),
        ),
    ]
