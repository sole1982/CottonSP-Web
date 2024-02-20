# Generated by Django 5.0.2 on 2024-02-19 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='productos/')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('resumen', models.TextField()),
            ],
        ),
    ]
