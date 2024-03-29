# Generated by Django 3.0.4 on 2020-04-09 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parametros', '0001_initial'),
        ('muestras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n1', models.CharField(blank=True, max_length=20, null=True)),
                ('n2', models.CharField(blank=True, max_length=20, null=True)),
                ('n3', models.CharField(blank=True, max_length=20, null=True)),
                ('n4', models.CharField(blank=True, max_length=20, null=True)),
                ('n5', models.CharField(blank=True, max_length=20, null=True)),
                ('muestra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='muestra_resultado', to='muestras.Muestra')),
                ('parametro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parametro_resultado', to='parametros.Parametro')),
            ],
        ),
    ]
