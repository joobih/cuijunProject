# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2015-12-26 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0008_auto_20151220_0728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boutiquelinedetails',
            name='may_pic_address',
        ),
        migrations.AddField(
            model_name='boutiqueline',
            name='may_pic_address',
            field=models.CharField(max_length=255, null=True, verbose_name='\u5730\u56fe\u5730\u5740'),
        ),
    ]
