# Generated by Django 3.0.3 on 2020-02-04 14:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_first_name', models.CharField(max_length=200)),
                ('artist_last_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facts.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Facts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fact', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facts.Song')),
            ],
        ),
    ]
