# Generated by Django 2.0.4 on 2018-04-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='apellidom',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro',
            name='apellidop',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro',
            name='email',
            field=models.EmailField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro',
            name='estado',
            field=models.CharField(choices=[('alumno', 'Alumno'), ('exalumno', 'Exalumno'), ('profesional', 'Profesional')], default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro',
            name='municipio',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro',
            name='nocontrol',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro',
            name='rfc',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro',
            name='tipo_registro',
            field=models.CharField(choices=[('alumno', 'Alumno'), ('exalumno', 'Exalumno'), ('profesional', 'Profesional')], default='', max_length=255),
            preserve_default=False,
        ),
    ]
