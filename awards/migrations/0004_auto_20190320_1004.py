# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-20 07:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0003_criteria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criteria',
            name='content',
        ),
        migrations.RemoveField(
            model_name='criteria',
            name='design',
        ),
        migrations.RemoveField(
            model_name='criteria',
            name='usability',
        ),
        migrations.DeleteModel(
            name='Criteria',
        ),
    ]