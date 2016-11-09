# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0003_auto_20161022_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('create_time', models.DateTimeField(help_text='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(help_text='更新时间', auto_now=True)),
                ('extinfo', jsonfield.fields.JSONField(help_text='扩展字段', default={}, blank=True, null=True)),
                ('goods_num', models.SmallIntegerField(help_text='商品数量', default=1)),
                ('goods', models.ForeignKey(help_text='商品', to='goods.Goods')),
                ('user', models.ForeignKey(help_text='用户', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 's_cart',
            },
        ),
    ]
