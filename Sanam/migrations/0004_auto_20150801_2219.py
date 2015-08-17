# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanam', '0003_auto_20150728_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='superCategory',
            field=models.ForeignKey(to='Sanam.Category', related_name='subcategories'),
        ),
    ]
