# Generated by Django 3.0 on 2019-12-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0017_auto_20191209_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='major',
            field=models.ManyToManyField(related_name='courses', to='forms.Major'),
        ),
    ]
