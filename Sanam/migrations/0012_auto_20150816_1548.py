# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0011_auto_20150816_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(to='Sanam.Category', related_name='eventsubcategories', auto_choose=True, chained_model_field='category', chained_field='category', null=True),
        ),
    ]
