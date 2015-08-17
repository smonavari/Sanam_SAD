# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0014_auto_20150816_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, to='Sanam.Subcategory', chained_model_field='superCategory', chained_field='category', null=True, related_name='eventsubcategories'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phoneNumber',
            field=models.CharField(max_length=20, default=1),
            preserve_default=False,
        ),
    ]
