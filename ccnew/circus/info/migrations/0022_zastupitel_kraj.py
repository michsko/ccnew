# Generated by Django 4.1.5 on 2023-01-26 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0021_remove_zastupitel_birth_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='zastupitel',
            name='kraj',
            field=models.CharField(default='p', max_length=255, verbose_name='kraj'),
        ),
    ]
