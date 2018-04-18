# Generated by Django 2.0.4 on 2018-04-17 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0006_ponente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conferencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('foto', models.ImageField(blank=True, upload_to='')),
                ('ponente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registro.Ponente')),
            ],
        ),
    ]