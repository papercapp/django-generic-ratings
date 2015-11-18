# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('key', models.CharField(max_length=16)),
                ('average', models.FloatField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('num_votes', models.PositiveIntegerField(default=0)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('key', models.CharField(max_length=16)),
                ('score', models.FloatField()),
                ('ip_address', models.IPAddressField(null=True)),
                ('cookie', models.CharField(max_length=64, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('user', models.ForeignKey(related_name='votes', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('content_type', 'object_id', 'key', 'ip_address', 'cookie'), ('content_type', 'object_id', 'key', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='score',
            unique_together=set([('content_type', 'object_id', 'key')]),
        ),
    ]
