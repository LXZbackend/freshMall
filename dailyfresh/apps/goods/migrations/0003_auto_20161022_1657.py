# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_goods_goods_subtitile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='goods_subtitile',
            new_name='goods_subtitle',
        ),
    ]
