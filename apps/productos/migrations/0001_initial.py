# Generated by Django 5.0.2 on 2024-02-23 22:26

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
                ('imagen_principal', models.ImageField(upload_to='productos/')),
                ('imagen_2', models.ImageField(blank=True, default='img/hero-banner.jpg', null=True, upload_to='productos/')),
                ('imagen_3', models.ImageField(blank=True, default='img/hero-banner.jpg', null=True, upload_to='productos/')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=256)),
                ('resumen', models.TextField(blank=True, max_length=256)),
                ('resumen_2', models.TextField(blank=True, max_length=256)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
