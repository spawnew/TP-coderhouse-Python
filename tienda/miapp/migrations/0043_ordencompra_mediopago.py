# Generated by Django 5.0.1 on 2024-03-10 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0042_ordencompra'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordencompra',
            name='mediopago',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
