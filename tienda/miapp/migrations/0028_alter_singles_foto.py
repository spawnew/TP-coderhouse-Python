# Generated by Django 5.0.1 on 2024-03-07 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0027_alter_producto_fproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singles',
            name='foto',
            field=models.ImageField(upload_to=''),
        ),
    ]