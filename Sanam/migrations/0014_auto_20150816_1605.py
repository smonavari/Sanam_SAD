# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0013_auto_20150816_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(related_name='eventsubcategories', chained_model_field='category', chained_field='category', auto_choose=True, to='Sanam.Subcategory', null=True),
        ),
    ]
