# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20161027_0139'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BrowseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间')),
                ('extinfo', jsonfield.fields.JSONField(default={}, help_text='扩展字段', blank=True, null=True)),
                ('goods', models.ForeignKey(to='goods.Goods', help_text='商品')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, help_text='用户')),
            ],
            options={
                'db_table': 's_user_browse_history',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间')),
                ('extinfo', jsonfield.fields.JSONField(default={}, help_text='扩展字段', blank=True, null=True)),
                ('user_id', models.IntegerField(help_text='用户ID')),
                ('user_type', models.SmallIntegerField(default=1, help_text='用户类型')),
                ('sex', models.IntegerField(default=3, help_text='性别')),
                ('realname', models.CharField(null=True, max_length=32, help_text='真实姓名', blank=True)),
                ('province', models.CharField(null=True, max_length=32, help_text='省', blank=True)),
                ('city', models.CharField(null=True, max_length=32, help_text='市', blank=True)),
                ('county', models.CharField(null=True, max_length=32, help_text='县', blank=True)),
                ('addr_detail', models.CharField(null=True, max_length=64, help_text='详细地址', blank=True)),
            ],
            options={
                'db_table': 's_user_profile',
            },
        ),
    ]
