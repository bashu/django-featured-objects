# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('slug', models.SlugField(unique=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'swappable': 'FEATURED_CATEGORY_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('object_id', models.IntegerField()),
                ('category', models.ForeignKey(to=settings.FEATURED_CATEGORY_MODEL, on_delete=models.CASCADE)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', on_delete=models.CASCADE)),
            ],
        ),
    ]
