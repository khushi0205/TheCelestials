# Generated by Django 3.2.8 on 2021-10-26 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsaii', '0003_post_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
