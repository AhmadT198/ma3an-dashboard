# Generated by Django 4.2 on 2023-04-26 00:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='hosts',
            field=models.ManyToManyField(related_name='HostedEvents', to=settings.AUTH_USER_MODEL),
        ),
    ]
