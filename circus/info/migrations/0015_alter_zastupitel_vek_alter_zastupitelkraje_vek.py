# Generated by Django 4.1.5 on 2023-01-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0014_alter_zastupitel_vek_alter_zastupitelkraje_vek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zastupitel',
            name='vek',
            field=models.CharField(blank=True, max_length=255, verbose_name='věk'),
        ),
        migrations.AlterField(
            model_name='zastupitelkraje',
            name='vek',
            field=models.CharField(blank=True, max_length=255, verbose_name='věk'),
        ),
    ]
