# Generated by Django 2.2.6 on 2019-11-06 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torpedopage', '0006_auto_20191106_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torpedo',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='torpedos/'),
        ),
    ]