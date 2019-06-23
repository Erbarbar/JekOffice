# Generated by Django 2.1.2 on 2019-06-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projetos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('descrição', models.TextField(verbose_name='Descrição')),
                ('data_inicio', models.DateField(auto_now=True, verbose_name='Data Criação')),
                ('estado', models.CharField(choices=[('Definition', 'Definition'), ('Initiation', 'Initiation'), ('Execution', 'Execution'), ('Monitoring & Control', 'Monitoring & Control'), ('Closure', 'Closure')], max_length=15, verbose_name='Estado')),
                ('data_fim', models.DateField(blank=True, null=True, verbose_name='Data Fim')),
                ('objectivo', models.CharField(choices=[('INTERNO', 'INTERNO'), ('EXTERNO', 'EXTERNO')], max_length=8, verbose_name='Objectivo')),
            ],
        ),
        migrations.CreateModel(
            name='Relatorios_formacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Relatorios_recrutamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(default=2019)),
                ('semestre', models.CharField(choices=[('1º Semestre', '1º Semestre'), ('2º Semestre', '2º Semestre')], max_length=11)),
                ('n_vagas_tec', models.IntegerField(default=0)),
                ('n_vagas_ino', models.IntegerField(default=0)),
                ('n_vagas_int', models.IntegerField(default=0)),
                ('n_candidatos', models.IntegerField(default=0)),
                ('n_grupos', models.IntegerField(default=0)),
                ('n_min_grupo', models.IntegerField(default=0)),
                ('n_max_grupo', models.IntegerField(default=0)),
                ('n_individual', models.IntegerField(default=0)),
                ('n_estagio', models.IntegerField(default=0)),
                ('n_admitidos', models.IntegerField(default=0)),
                ('documento', models.FileField(blank=True, null=True, upload_to='relatorios/')),
            ],
        ),
    ]
