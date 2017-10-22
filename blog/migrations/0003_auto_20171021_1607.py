# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171020_2346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-time']},
        ),
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='blog',
            name='picture',
            field=models.CharField(default='../static/picture/<django.db.models.fields.IntegerField>.jpg', max_length=150, verbose_name='配图地址'),
        ),
    ]
