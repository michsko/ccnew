# Generated by Django 4.1.5 on 2023-01-25 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_alter_zastupitel_title_alter_zastupitelkraje_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zastupitel',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Titul'),
        ),
        migrations.AlterField(
            model_name='zastupitelkraje',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Titul'),
        ),
    ]
