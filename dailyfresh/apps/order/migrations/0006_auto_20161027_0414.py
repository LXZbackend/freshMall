# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_sorder_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sorder',
            name='comment',
        ),
        migrations.AddField(
            model_name='sordergoods',
            name='comment',
            field=models.TextField(default='', help_text='商品评价'),
        ),
    ]
