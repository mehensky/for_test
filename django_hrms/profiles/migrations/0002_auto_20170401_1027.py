# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='attendance_date',
            new_name='attendance_data',
        ),
        migrations.AlterField(
            model_name='attendance_data',
            name='attendance_day',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='employee_id',
            field=models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='attendance_data',
            unique_together=set([('employee_id', 'attendance_day')]),
        ),
    ]
