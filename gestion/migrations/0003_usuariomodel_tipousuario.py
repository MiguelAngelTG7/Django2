# Generated by Django 5.1.2 on 2024-11-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_usuariomodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariomodel',
            name='tipoUsuario',
            field=models.CharField(choices=[('ADMIN', 'ADMIN'), ('TRABAJADOR', 'TRABAJADOR')], db_column='tipo_usuario', default='ADMIN', max_length=100),
        ),
    ]
