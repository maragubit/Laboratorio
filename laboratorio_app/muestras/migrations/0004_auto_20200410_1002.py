# Generated by Django 3.0.4 on 2020-04-10 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muestras', '0003_remove_muestra_rango'),
    ]

    operations = [
        migrations.AddField(
            model_name='muestra',
            name='idfinal',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='muestra',
            name='idinicial',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
