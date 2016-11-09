# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20160819_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='update_time',
            field=models.DateTimeField(auto_now=True, help_text='更新时间'),
        ),
    ]
