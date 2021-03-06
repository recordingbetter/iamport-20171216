# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-16 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='상품명')),
                ('desc', models.TextField(blank=True)),
                ('amount', models.PositiveIntegerField(verbose_name='결제금액')),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
