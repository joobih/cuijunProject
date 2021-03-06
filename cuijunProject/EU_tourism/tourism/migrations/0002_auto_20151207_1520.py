# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2015-12-07 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boutiqueline',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='boutiquelinedetails',
            name='approach',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='boutiquelinedetails',
            name='detail_pic_address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='boutiquelinedetails',
            name='detail_pic_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='boutiquelinedetails',
            name='may_pic_address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='boutiquelinedetails',
            name='node_details',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='privateorder',
            name='approach',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='privateorder',
            name='days',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='privateorder',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='privateorder',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
