# Generated by Django 3.2.3 on 2021-08-04 16:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0011_auto_20210803_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 6, 16, 54, 39, 383389, tzinfo=utc)),
        ),
    ]
