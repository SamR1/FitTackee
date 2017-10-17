# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 07:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0008_auto_20171016_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='activity_users_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='comment_users_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
