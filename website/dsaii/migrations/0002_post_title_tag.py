# Generated by Django 3.2.8 on 2021-10-26 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsaii', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Awesome BLogs', max_length=255),
        ),
    ]
