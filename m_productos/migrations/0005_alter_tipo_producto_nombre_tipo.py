# Generated by Django 4.2.2 on 2023-06-24 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m_productos', '0004_alter_tipo_producto_nombre_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_producto',
            name='nombre_tipo',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
