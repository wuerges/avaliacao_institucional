# Generated by Django 3.0 on 2019-12-09 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0018_auto_20191209_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questiontemplate',
            name='question_type',
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('GERAL', 'Pergunta geral sobre a instituição'), ('CURSO', 'Pergunta geral do curso'), ('DISC', 'Pergunta para disciplinas'), ('PROF', 'Pergunta para professor'), ('COORD', 'Pergunta para coordenação')], default='DISC', max_length=5),
            preserve_default=False,
        ),
    ]
