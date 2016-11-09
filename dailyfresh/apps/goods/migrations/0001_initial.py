# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(help_text='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间')),
                ('extinfo', jsonfield.fields.JSONField(help_text='扩展字段', default={}, null=True, blank=True)),
                ('goods_type_id', models.SmallIntegerField(help_text='商品分类ID', default=1)),
                ('goods_name', models.CharField(max_length=64, help_text='商品名称', default='')),
                ('goods_price', models.FloatField(help_text='商品价格', default=0.0)),
                ('goods_unit', models.IntegerField(help_text='商品单位', default=1)),
                ('goods_ex_price', models.FloatField(help_text='商品运费', default=0.0)),
                ('goods_info', models.TextField(help_text='商品描述')),
                ('goods_status', models.IntegerField(help_text='商品状态', default=1)),
            ],
            options={
                'db_table': 's_goods',
            },
        ),
    ]
