# Generated by Django 2.0.4 on 2018-05-31 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0021_conferencia_requisitos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencia',
            name='requisitos',
            field=models.CharField(max_length=255),
        ),
    ]
