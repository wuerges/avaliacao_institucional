# Generated by Django 3.0 on 2019-12-09 03:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0015_auto_20191209_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='major',
            field=models.ManyToManyField(related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
