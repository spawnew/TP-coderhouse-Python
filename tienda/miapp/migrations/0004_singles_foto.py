# Generated by Django 5.0.1 on 2024-03-02 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_productosellado_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='singles',
            name='foto',
            field=models.ImageField(default='../media/avatares/1.jpeg', upload_to='media/avatares'),
        ),
    ]
