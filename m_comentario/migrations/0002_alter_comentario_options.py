# Generated by Django 4.2 on 2023-06-30 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('m_comentario', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'ordering': ['id'], 'verbose_name': 'coment', 'verbose_name_plural': 'comentarios'},
        ),
    ]