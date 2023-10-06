# Generated by Django 4.2.2 on 2023-06-25 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m_venta', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detalle_venta',
            options={'ordering': ['id'], 'verbose_name': 'detalle_pedidos'},
        ),
        migrations.AlterModelOptions(
            name='venta',
            options={'ordering': ['id'], 'verbose_name': 'pedidos'},
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='valor_producto',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detalle_venta',
            name='cant_producto',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterModelTable(
            name='detalle_venta',
            table='detalle_venta',
        ),
        migrations.AlterModelTable(
            name='venta',
            table='venta',
        ),
    ]