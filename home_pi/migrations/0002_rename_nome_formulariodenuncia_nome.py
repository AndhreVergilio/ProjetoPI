# Generated by Django 5.0.4 on 2024-04-20 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_pi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formulariodenuncia',
            old_name='nome',
            new_name='Nome',
        ),
    ]