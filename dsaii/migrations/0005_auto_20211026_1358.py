# Generated by Django 3.2.8 on 2021-10-26 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsaii', '0004_alter_post_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_date',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
