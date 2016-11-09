# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorder',
            name='order_status',
            field=models.SmallIntegerField(default=1, help_text='订单状态'),
        ),
        migrations.AlterField(
            model_name='sorder',
            name='payment_method',
            field=models.SmallIntegerField(default=1, help_text='支付方式'),
        ),
    ]
