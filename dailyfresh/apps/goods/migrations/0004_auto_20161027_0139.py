# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20161022_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_sales',
            field=models.IntegerField(help_text='商品销量', default=1),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_stock',
            field=models.IntegerField(help_text='商品库存', default=1),
        ),
    ]
