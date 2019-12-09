# Generated by Django 3.0 on 2019-12-09 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0020_auto_20191209_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsubmission',
            name='text_answer',
            field=models.CharField(default='resposta padrao', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formsubmission',
            name='text_question',
            field=models.CharField(default='pergunta padrao', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formsubmission',
            name='form_application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='submissions', to='forms.FormApplication'),
        ),
        migrations.AlterField(
            model_name='formsubmission',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='submissions', to='forms.Professor'),
        ),
    ]
