# Generated by Django 3.0.6 on 2020-05-17 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200516_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicsHappie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictitle', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to='portfolio/images/')),
                ('picdate', models.DateField()),
            ],
        ),
    ]
