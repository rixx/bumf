# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 22:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170106_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('variant', models.CharField(choices=[('budget', 'budget'), ('liability', 'liability'), ('income', 'income'), ('expense', 'expense')], default='budget', max_length=9)),
                ('comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='child_accounts', to='core.VirtualAccount')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='virtual_accounts', to='core.Project')),
            ],
        ),
    ]
