# Generated by Django 3.0.6 on 2020-05-16 10:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200515_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 5, 16, 10, 26, 38, 995984, tzinfo=utc)),
        ),
    ]
