# Generated by Django 5.0.1 on 2024-03-07 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0024_alter_producto_fproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fproducto',
            field=models.ImageField(default='media/avatares/1.jpeg', upload_to='media/avatares'),
        ),
    ]
