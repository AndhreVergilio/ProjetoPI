# Generated by Django 5.0.4 on 2024-05-16 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_pi', '0007_alter_formulariodenuncia_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulariodenuncia',
            name='Foto',
            field=models.ImageField(default='media/osint.png', upload_to='media/'),
        ),
    ]
