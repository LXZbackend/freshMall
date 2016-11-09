# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='recipient_name',
            field=models.CharField(max_length=32, null=True, help_text='收件人姓名', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='recipient_phone',
            field=models.CharField(max_length=11, null=True, help_text='收件人电话', blank=True),
            preserve_default=True,
        ),
    ]
