# Generated by Django 2.0.4 on 2018-05-16 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0012_ponente_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='institucion',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registro',
            name='semestre',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=255),
        ),
        migrations.AlterField(
            model_name='registro',
            name='telefono',
            field=models.CharField(max_length=10),
        ),
    ]
