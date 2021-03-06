# Generated by Django 3.0.3 on 2020-02-05 11:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='artist_first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='song_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='artist_last_name',
        ),
        migrations.RemoveField(
            model_name='facts',
            name='author',
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='facts.Artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
