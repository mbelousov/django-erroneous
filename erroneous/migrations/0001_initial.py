# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.CharField(db_index=True, max_length=128, null=True, verbose_name='type', blank=True)),
                ('info', models.TextField()),
                ('data', models.TextField(null=True, blank=True)),
                ('path', models.URLField(null=True, blank=True)),
                ('when', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('html', models.TextField(null=True, blank=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Error',
                'verbose_name_plural': 'Errors',
            },
            bases=(models.Model,),
        ),
    ]
