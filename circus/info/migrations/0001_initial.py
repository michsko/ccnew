# Generated by Django 4.1.5 on 2023-01-23 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObceCr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obec', models.CharField(max_length=255, verbose_name='Obec')),
                ('kod_obce', models.CharField(max_length=255, verbose_name='Kod obce')),
                ('okres', models.CharField(max_length=255, verbose_name='Okres ')),
                ('kod_okresu', models.CharField(max_length=255, verbose_name='Kod okresu')),
                ('kraj', models.CharField(max_length=255, verbose_name='Kraj')),
                ('kod_kraje', models.CharField(max_length=255, verbose_name='Kod kraje')),
                ('psc', models.CharField(max_length=255, verbose_name='PSC')),
                ('latitude', models.FloatField(max_length=255, verbose_name='Latitude')),
                ('longitude', models.FloatField(max_length=255, verbose_name='Longitude')),
            ],
        ),
    ]
