# Generated by Django 2.0.4 on 2018-05-23 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0016_auto_20180523_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencia',
            name='duracion',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=5, null=True),
        ),
    ]
