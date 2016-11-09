# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('create_time', models.DateTimeField(help_text='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(help_text='更新时间', auto_now_add=True, auto_now=True)),
                ('extinfo', jsonfield.fields.JSONField(help_text='扩展字段', blank=True, null=True, default={})),
                ('user_id', models.IntegerField(help_text='用户ID')),
                ('province', models.CharField(help_text='省', blank=True, null=True, max_length=32)),
                ('city', models.CharField(help_text='市', blank=True, null=True, max_length=32)),
                ('county', models.CharField(help_text='县', blank=True, null=True, max_length=32)),
                ('addr_detail', models.CharField(help_text='详细地址', blank=True, null=True, max_length=64)),
            ],
            options={
                'db_table': 's_address',
            },
            bases=(models.Model,),
        ),
    ]
