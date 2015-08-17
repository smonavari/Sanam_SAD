# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0010_auto_20150816_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(to='Sanam.Category', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(null=True, auto_choose=True, to='Sanam.Subcategory', chained_field='category', chained_model_field='category', related_name='eventsubcategories'),
        ),
    ]
