# Generated by Django 2.0.4 on 2018-05-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0015_conferencia_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferencia',
            name='hora_fin',
            field=models.TimeField(default='00:00:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conferencia',
            name='fecha_hora',
            field=models.DateField(default='2018-05-23'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conferencia',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='conferencia',
            name='hora',
            field=models.TimeField(default='00:00:00'),
            preserve_default=False,
        ),
    ]