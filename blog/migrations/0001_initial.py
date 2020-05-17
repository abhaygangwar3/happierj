# Generated by Django 3.0.6 on 2020-05-15 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('images', models.ImageField(upload_to='blog/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
