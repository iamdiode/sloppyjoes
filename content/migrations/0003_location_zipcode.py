# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='zipcode',
            field=models.CharField(null=True, blank=True, max_length=12),
            preserve_default=True,
        ),
    ]
