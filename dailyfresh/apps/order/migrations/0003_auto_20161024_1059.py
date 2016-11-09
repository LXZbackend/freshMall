# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20161024_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorder',
            name='ex_price',
            field=models.FloatField(default=10.0, help_text='商品运费'),
        ),
    ]
