# Generated by Django 4.1.5 on 2023-01-30 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0023_volebvyslprez2023obec2kolo'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolebVyslPrez2023Obec1kolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cislo_obce', models.CharField(max_length=255, verbose_name='Číslo obce')),
                ('nazev_obce', models.CharField(max_length=255, verbose_name='Jméno obce')),
                ('hlasy_Fischer', models.CharField(max_length=255, verbose_name='Hlasy Pavel Fischer')),
                ('hlasy_Basta', models.CharField(max_length=255, verbose_name='Hlasy Jaroslav Bašta')),
                ('hlasy_Pavel', models.CharField(max_length=255, verbose_name='Hlasy Petr Pavel')),
                ('hlasy_Zima', models.CharField(max_length=255, verbose_name='Hlasy Tomáš Zima')),
                ('hlasy_Nerudova', models.CharField(max_length=255, verbose_name='Hlasy Danuše Nerudová')),
                ('hlasy_Babis', models.CharField(max_length=255, verbose_name='Hlasy Andrej Babiš')),
                ('hlasy_Divis', models.CharField(max_length=255, verbose_name='Hlasy Karel Diviš')),
                ('hlasy_Hilser', models.CharField(max_length=255, verbose_name='Hlasy Marek Hilšer')),
                ('ucast_procenta', models.CharField(max_length=255, verbose_name='Účast v procentech')),
                ('platne_hlasy', models.CharField(max_length=255, verbose_name='Platné hlasy')),
                ('plat_hlas_procenta', models.CharField(max_length=255, verbose_name='Platné hlasy v procentech')),
                ('ucast_proc', models.CharField(max_length=255, verbose_name='Účast v procentech')),
                ('zapsani_volici', models.CharField(max_length=255, verbose_name='Zapsaní voliči')),
            ],
        ),
        migrations.AlterField(
            model_name='volebvyslprez2023obec2kolo',
            name='hlasy_Babis',
            field=models.CharField(max_length=255, verbose_name='Hlasy Andrej Babiš'),
        ),
    ]