# Generated by Django 5.0.1 on 2024-03-06 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0017_rename_nombre_cliente_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fproducto',
            field=models.ImageField(upload_to='media/avatares'),
        ),
    ]
