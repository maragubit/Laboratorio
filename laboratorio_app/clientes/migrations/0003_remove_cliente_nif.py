# Generated by Django 3.0.4 on 2020-04-15 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20200415_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='nif',
        ),
    ]
