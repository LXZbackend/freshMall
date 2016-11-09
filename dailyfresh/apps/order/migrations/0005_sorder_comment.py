# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20161024_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='sorder',
            name='comment',
            field=models.TextField(default='', help_text='订单评价'),
        ),
    ]
