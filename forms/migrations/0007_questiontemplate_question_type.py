# Generated by Django 3.0 on 2019-12-09 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_formapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='questiontemplate',
            name='question_type',
            field=models.CharField(choices=[('GERAL', 'Pergunta geral sobre a instituição'), ('CURSO', 'Pergunta geral do curso'), ('DISC', 'Pergunta para disciplinas'), ('PROF', 'Pergunta para professor'), ('COORD', 'Pergunta para coordenação')], default='DISC', max_length=5),
            preserve_default=False,
        ),
    ]
