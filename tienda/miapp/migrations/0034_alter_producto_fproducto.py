# Generated by Django 5.0.1 on 2024-03-09 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0033_alter_producto_fproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fproducto',
            field=models.ImageField(default='avatares/default_1.jpeg', upload_to='avatares'),
        ),
    ]
