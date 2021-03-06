# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 02:47
from __future__ import unicode_literals

import Athena.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text=b'Nome do Aluno', max_length=50)),
                ('user', models.ForeignKey(help_text=b'Usuario de login relacionado ao Aluno', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=1000)),
                ('arquivo_roteiro', models.FileField(upload_to=Athena.models.atividade_path)),
                ('arquivo_entrada', models.FileField(upload_to=Athena.models.atividade_path)),
                ('arquivo_saida', models.FileField(upload_to=Athena.models.atividade_path)),
                ('data_limite', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text=b'Nome do Professor', max_length=50)),
                ('user', models.ForeignKey(help_text=b'Usuario de login relacionado ao Professor', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RelAlunoAtividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foiEntregue', models.BooleanField(help_text=b'Se o aluno ja mandou alguma submissao para a atividade')),
                ('aluno', models.ForeignKey(help_text=b'Aluno inscrito na atividade', on_delete=django.db.models.deletion.CASCADE, to='Athena.Aluno')),
                ('atividade', models.ForeignKey(help_text=b'Atividade do aluno', on_delete=django.db.models.deletion.CASCADE, to='Athena.Atividade')),
            ],
        ),
        migrations.CreateModel(
            name='Submissao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_envio', models.DateField(auto_now=True, help_text=b'Data de submissao do codigo')),
                ('arquivo_codigo', models.FileField(upload_to=Athena.models.submissao_path)),
                ('resultado', models.CharField(choices=[(b'AC', b'Aceito'), (b'TLE', b'Tempo Limite Excedido'), (b'RTE', b'Erro em tempo de execucao'), (b'CE', b'Erro de compilacao'), (b'WA', b'Resposta Errada')], help_text=b'Resultado da submissao do aluno', max_length=3)),
                ('nota', models.PositiveSmallIntegerField(help_text=b'Nota para submissao do aluno')),
                ('aluno', models.ForeignKey(help_text=b'Aluno que enviou a submissao', on_delete=django.db.models.deletion.CASCADE, to='Athena.Aluno')),
                ('atividade', models.ForeignKey(help_text=b'Atividade relacionada a submissao', on_delete=django.db.models.deletion.CASCADE, to='Athena.Atividade')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=2000)),
                ('alunos', models.ManyToManyField(blank=True, help_text=b'Alunos inscritos na turma', to='Athena.Aluno')),
                ('professor', models.ForeignKey(help_text=b'Professor da Turma', on_delete=django.db.models.deletion.CASCADE, to='Athena.Professor')),
            ],
        ),
        migrations.AddField(
            model_name='atividade',
            name='alunos',
            field=models.ManyToManyField(blank=True, help_text=b'Relacao do aluno com a atividade,\n            guarda se aluno submeteu atividade', through='Athena.RelAlunoAtividade', to='Athena.Aluno'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='turma',
            field=models.ForeignKey(help_text=b'Turma a qual a atividade pertence', on_delete=django.db.models.deletion.CASCADE, to='Athena.Turma'),
        ),
    ]
