# Generated by Django 2.0.4 on 2018-04-26 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0011_ponente_resumen'),
    ]

    operations = [
        migrations.AddField(
            model_name='ponente',
            name='activo',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]