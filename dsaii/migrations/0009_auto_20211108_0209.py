# Generated by Django 3.2.8 on 2021-11-07 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dsaii', '0008_evecomm'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='author',
            field=models.CharField(default='Awesome BLogs', max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]