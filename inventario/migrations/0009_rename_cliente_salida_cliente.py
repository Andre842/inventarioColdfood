# Generated by Django 5.1.3 on 2024-11-09 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0008_cliente_remove_salida_proveedor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salida',
            old_name='Cliente',
            new_name='cliente',
        ),
    ]
