# Generated by Django 4.2.16 on 2024-11-22 00:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adote', '0002_remove_animal_idade_animal_idade_anos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='adotante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
