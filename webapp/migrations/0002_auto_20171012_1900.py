# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoxNumb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='card',
            name='BoxNumber',
        ),
        migrations.AlterField(
            model_name='card',
            name='SubjectName',
            field=models.CharField(db_index=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='BoxNumber',
            field=models.ManyToManyField(to='webapp.BoxNumb'),
        ),
    ]