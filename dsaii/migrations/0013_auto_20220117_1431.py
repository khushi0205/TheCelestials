# Generated by Django 3.2.8 on 2022-01-17 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsaii', '0012_auto_20211108_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dd',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='mm',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='yy',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
