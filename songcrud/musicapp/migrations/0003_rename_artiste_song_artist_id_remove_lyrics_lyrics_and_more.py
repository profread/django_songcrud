# Generated by Django 4.1.2 on 2022-10-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_alter_artist_first_name_alter_artist_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='Artiste',
            new_name='artist_id',
        ),
        migrations.RemoveField(
            model_name='lyrics',
            name='lyrics',
        ),
        migrations.AlterField(
            model_name='lyrics',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='lyrics',
            name='song_id',
            field=models.IntegerField(),
        ),
    ]