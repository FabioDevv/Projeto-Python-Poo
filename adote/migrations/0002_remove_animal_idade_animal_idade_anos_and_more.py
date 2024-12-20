# Generated by Django 4.2.16 on 2024-11-17 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='idade',
        ),
        migrations.AddField(
            model_name='animal',
            name='idade_anos',
            field=models.PositiveIntegerField(blank=True, help_text='Preencha apenas se a idade estiver em anos.', null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='idade_meses',
            field=models.PositiveIntegerField(blank=True, help_text='Preencha apenas se a idade estiver em meses.', null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='sexo',
            field=models.CharField(choices=[('M', 'Macho'), ('F', 'Fêmea')], default='M', max_length=1),
        ),
    ]
