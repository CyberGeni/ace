# Generated by Django 3.2.6 on 2021-10-28 21:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workspace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='contributors',
            field=models.ManyToManyField(blank=True, related_name='contributors', to=settings.AUTH_USER_MODEL),
        ),
    ]
