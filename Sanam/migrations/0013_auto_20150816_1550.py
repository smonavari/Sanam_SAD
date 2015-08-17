# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0012_auto_20150816_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(default=1, to='Sanam.Subcategory', chained_field='category', chained_model_field='category'),
            preserve_default=False,
        ),
    ]
