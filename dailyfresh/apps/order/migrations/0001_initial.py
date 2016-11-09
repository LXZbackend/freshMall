# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0004_auto_20161024_0952'),
        ('goods', '0003_auto_20161022_1657'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('update_time', models.DateTimeField(help_text='更新时间', auto_now=True)),
                ('extinfo', jsonfield.fields.JSONField(blank=True, null=True, help_text='扩展字段', default={})),
                ('total_amount', models.FloatField(help_text='订单总额', default=0.0)),
                ('total_count', models.SmallIntegerField(help_text='订单商品数量', default=1)),
                ('ex_price', models.FloatField(help_text='商品运费', default=0.0)),
                ('payment_method', models.SmallIntegerField(help_text='支付方式')),
                ('order_status', models.SmallIntegerField(help_text='订单状态')),
                ('addr', models.ForeignKey(to='address.Address', help_text='地址')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, help_text='用户')),
            ],
            options={
                'db_table': 's_order',
            },
        ),
        migrations.CreateModel(
            name='SOrderGoods',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('update_time', models.DateTimeField(help_text='更新时间', auto_now=True)),
                ('extinfo', jsonfield.fields.JSONField(blank=True, null=True, help_text='扩展字段', default={})),
                ('goods_price', models.FloatField(help_text='商品单价', default=0.0)),
                ('goods_count', models.SmallIntegerField(help_text='商品数量', default=1)),
                ('goods_id', models.ForeignKey(to='goods.Goods', help_text='商品')),
                ('sorder', models.ForeignKey(to='order.SOrder', help_text='订单')),
            ],
            options={
                'db_table': 's_order_goods',
            },
        ),
    ]
