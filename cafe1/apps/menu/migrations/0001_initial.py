# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-15 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('kind', models.CharField(choices=[('english', '英国紅茶'), ('chinese', '中国茶'), ('japanese', '日本茶')], max_length=255, verbose_name='種類')),
            ],
        ),
    ]
