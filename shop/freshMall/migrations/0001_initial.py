# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='consignee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recePerName', models.CharField(max_length=20)),
                ('recrPerTel', models.CharField(max_length=11)),
                ('addr', models.CharField(max_length=1000)),
                ('postcode', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='goodsClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('className', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='goodsList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goodsName', models.CharField(max_length=50)),
                ('goodsDetail', models.CharField(max_length=1000)),
                ('goodsRoute', models.CharField(max_length=50)),
                ('goodsStock', models.CharField(max_length=50)),
                ('goodsPrice', models.DecimalField(max_digits=6, decimal_places=2)),
                ('goodsType', models.ForeignKey(to='freshMall.goodsClass')),
            ],
        ),
        migrations.CreateModel(
            name='orderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderId', models.IntegerField()),
                ('goodsCount', models.IntegerField()),
                ('orderSum', models.DecimalField(max_digits=6, decimal_places=2)),
                ('isPay', models.BooleanField()),
                ('goodsId', models.ForeignKey(to='freshMall.goodsList')),
            ],
        ),
        migrations.CreateModel(
            name='orderForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='shoppingCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('total', models.FloatField()),
                ('goodsId', models.ForeignKey(to='freshMall.goodsList')),
            ],
        ),
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account', models.CharField(max_length=20)),
                ('passswd', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=30)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='userInfo',
            field=models.ForeignKey(to='freshMall.userInfo'),
        ),
        migrations.AddField(
            model_name='orderform',
            name='userId',
            field=models.ForeignKey(to='freshMall.userInfo'),
        ),
        migrations.AddField(
            model_name='consignee',
            name='userNum',
            field=models.ForeignKey(to='freshMall.userInfo'),
        ),
    ]
