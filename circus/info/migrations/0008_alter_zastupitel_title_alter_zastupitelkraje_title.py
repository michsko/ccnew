# Generated by Django 4.1.5 on 2023-01-25 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_remove_zastupitel_titel_remove_zastupitelkraje_titel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zastupitel',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Titul '),
        ),
        migrations.AlterField(
            model_name='zastupitelkraje',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Titul '),
        ),
    ]
