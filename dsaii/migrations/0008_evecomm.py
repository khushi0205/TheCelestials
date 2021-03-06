# Generated by Django 3.2.8 on 2021-11-07 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dsaii', '0007_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='EveComm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Body', models.TextField()),
                ('Date_added', models.DateTimeField(auto_now_add=True)),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evecomm', to='dsaii.post')),
            ],
        ),
    ]
