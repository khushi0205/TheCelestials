# Generated by Django 3.2.8 on 2021-11-07 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsaii', '0010_auto_20211108_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.CharField(default='Enter date here', max_length=255),
        ),
    ]
