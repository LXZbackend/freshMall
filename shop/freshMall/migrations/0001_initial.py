# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consignee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recePerName', models.CharField(max_length=20)),
                ('recePerTel', models.CharField(max_length=11)),
                ('addr', models.CharField(max_length=1000)),
                ('postCode', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('className', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goodsName', models.CharField(max_length=50)),
                ('goodsResume', models.CharField(max_length=80)),
                ('goodsDetail', tinymce.models.HTMLField()),
                ('goodsRoute', models.ImageField(upload_to=b'uploads/')),
                ('goodsStock', models.CharField(max_length=50)),
                ('goodsPrice', models.DecimalField(max_digits=6, decimal_places=2)),
                ('buyTimes', models.IntegerField()),
                ('goodsUnit', models.CharField(max_length=20)),
                ('goodsPubdate', models.DateTimeField()),
                ('goodsType', models.ForeignKey(to='freshMall.GoodsClass')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goodsCount', models.IntegerField()),
                ('orderSum', models.DecimalField(max_digits=6, decimal_places=2)),
                ('isPay', models.BooleanField()),
                ('goodsId', models.ForeignKey(to='freshMall.GoodsList')),
            ],
        ),
        migrations.CreateModel(
            name='OrderForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderDate', models.DateTimeField()),
                ('orderNum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c', models.IntegerField()),
                ('total', models.FloatField()),
                ('isDelete', models.BooleanField(default=False)),
                ('goodsId', models.ForeignKey(to='freshMall.GoodsList')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account', models.CharField(max_length=20)),
                ('passswd', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='userId',
            field=models.ForeignKey(to='freshMall.UserInfo'),
        ),
        migrations.AddField(
            model_name='orderform',
            name='userId',
            field=models.ForeignKey(to='freshMall.UserInfo'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='orderId',
            field=models.ForeignKey(to='freshMall.OrderForm'),
        ),
        migrations.AddField(
            model_name='consignee',
            name='userNum',
            field=models.ForeignKey(to='freshMall.UserInfo'),
        ),
    ]
