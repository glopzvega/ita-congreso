# Generated by Django 2.0.4 on 2018-06-19 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0042_registro_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taller',
            name='objetivo',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taller',
            name='salon',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
