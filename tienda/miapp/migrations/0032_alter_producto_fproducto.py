# Generated by Django 5.0.1 on 2024-03-08 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0031_alter_producto_fproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fproducto',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
