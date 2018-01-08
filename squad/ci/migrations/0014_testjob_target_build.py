# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_project_enabled_plugins_list'),
        ('ci', '0013_testjob_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='testjob',
            name='target_build',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_jobs', to='core.Build'),
        ),
    ]