# Generated by Django 5.0.1 on 2024-03-05 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0013_singles_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fproducto',
            field=models.ImageField(upload_to='media/avatares'),
        ),
    ]
