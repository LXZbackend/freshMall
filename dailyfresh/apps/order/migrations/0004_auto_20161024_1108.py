# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20161024_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sordergoods',
            old_name='goods_id',
            new_name='goods',
        ),
    ]
