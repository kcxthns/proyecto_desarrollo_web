# Generated by Django 2.2.6 on 2019-11-17 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torpedopage', '0007_auto_20191106_0646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apunte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('documento', models.FileField(upload_to='media/documents')),
            ],
        ),
        migrations.DeleteModel(
            name='Torpedo',
        ),
    ]
