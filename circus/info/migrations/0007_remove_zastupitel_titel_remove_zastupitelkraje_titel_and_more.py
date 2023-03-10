# Generated by Django 4.1.5 on 2023-01-25 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_zastupitel_funkce_zastupitel_poznamky_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zastupitel',
            name='titel',
        ),
        migrations.RemoveField(
            model_name='zastupitelkraje',
            name='titel',
        ),
        migrations.AddField(
            model_name='zastupitel',
            name='birth_day',
            field=models.IntegerField(blank=True, default=None, verbose_name='den narození'),
        ),
        migrations.AddField(
            model_name='zastupitel',
            name='birth_month',
            field=models.IntegerField(blank=True, default=None, verbose_name='mesic narození'),
        ),
        migrations.AddField(
            model_name='zastupitel',
            name='birth_year',
            field=models.IntegerField(blank=True, default=None, verbose_name='rok narození'),
        ),
        migrations.AddField(
            model_name='zastupitel',
            name='title',
            field=models.CharField(default=None, max_length=255, verbose_name='Titul '),
        ),
        migrations.AddField(
            model_name='zastupitelkraje',
            name='birth_day',
            field=models.IntegerField(blank=True, default=None, verbose_name='den narození'),
        ),
        migrations.AddField(
            model_name='zastupitelkraje',
            name='birth_month',
            field=models.IntegerField(blank=True, default=None, verbose_name='mesic narození'),
        ),
        migrations.AddField(
            model_name='zastupitelkraje',
            name='birth_year',
            field=models.IntegerField(blank=True, default=None, verbose_name='rok narození'),
        ),
        migrations.AddField(
            model_name='zastupitelkraje',
            name='title',
            field=models.CharField(default=None, max_length=255, verbose_name='Titul '),
        ),
    ]
