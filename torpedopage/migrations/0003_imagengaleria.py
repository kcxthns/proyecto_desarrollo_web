# Generated by Django 2.2.6 on 2019-10-17 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torpedopage', '0002_imagenpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenGaleria',
            fields=[
                ('nombre', models.CharField(help_text='Debe contener la palabra galeria', max_length=200, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(help_text='Descripción que aparecerá al pie de la foto en la galería', max_length=250)),
                ('imagen', models.ImageField(upload_to='media/galeria')),
            ],
        ),
    ]
