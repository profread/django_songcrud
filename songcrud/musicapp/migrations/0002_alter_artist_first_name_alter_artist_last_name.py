# Generated by Django 4.1.2 on 2022-10-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='first_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='artist',
            name='last_name',
            field=models.CharField(max_length=40),
        ),
    ]
