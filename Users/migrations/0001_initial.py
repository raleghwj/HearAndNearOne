# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phoneNum', models.CharField(max_length=15)),
                ('sex', models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('ages', models.CharField(max_length=3, blank=True)),
                ('headImg', models.URLField(max_length=100, blank=True)),
                ('stat', models.CharField(default=b'S0A', max_length=5, choices=[(b'S0A', b'S0A'), (b'S0B', b'S0B'), (b'S0C', b'S0C'), (b'S0X', b'S0X')])),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
    ]
