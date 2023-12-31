# Generated by Django 4.2 on 2023-06-30 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('m_productos', '0009_alter_producto_img_producto_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_comentario', models.CharField(max_length=50)),
                ('contenido_comentario', models.TextField(max_length=500)),
                ('fecha_comentario', models.DateTimeField(auto_now_add=True)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m_productos.producto')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'coment',
                'verbose_name_plural': 'tipo productos',
                'db_table': 'comentarios',
                'ordering': ['id'],
            },
        ),
    ]
