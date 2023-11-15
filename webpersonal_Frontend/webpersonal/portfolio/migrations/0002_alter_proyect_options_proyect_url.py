# Generated by Django 4.2.3 on 2023-10-10 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proyect',
            options={'ordering': ['created'], 'verbose_name': 'proyecto', 'verbose_name_plural': 'proyectos'},
        ),
        migrations.AddField(
            model_name='proyect',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Dirección web'),
        ),
    ]
