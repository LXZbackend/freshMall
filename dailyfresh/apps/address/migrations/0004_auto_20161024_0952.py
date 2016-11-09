# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('address', '0003_auto_20161019_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user_id',
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(default=1, help_text='用户', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.CharField(help_text='邮编', max_length=10, blank=True, null=True),
        ),
    ]
