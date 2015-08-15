# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0006_auto_20150804_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='subcategory',
            field=models.ForeignKey(to='Sanam.Subcategory', related_name='eventsubcategories'),
        ),
    ]
