# Generated by Django 3.0.4 on 2020-04-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='proxima_visita',
            field=models.DateField(blank=True, null=True),
        ),
    ]