# Generated by Django 3.2.8 on 2021-11-07 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dsaii', '0009_auto_20211108_0209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='author',
            new_name='byline',
        ),
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
    ]
