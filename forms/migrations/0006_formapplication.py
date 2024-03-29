# Generated by Django 3.0 on 2019-12-09 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_offer_professors'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_template', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms.FormTemplate')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms.Semester')),
            ],
        ),
    ]
