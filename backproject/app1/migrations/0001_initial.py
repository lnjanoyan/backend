# Generated by Django 5.1.3 on 2024-11-23 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('isbn', models.CharField(max_length=500)),
                ('authors', models.CharField(max_length=500)),
                ('numberOfPages', models.IntegerField()),
                ('publisher', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=500)),
                ('mediaType', models.CharField(max_length=500)),
                ('released', models.CharField(max_length=500)),
                ('characters', models.CharField(max_length=500)),
                ('povCharacters', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Characters583',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=500)),
                ('gender', models.CharField(max_length=500)),
                ('culture', models.CharField(max_length=500)),
                ('born', models.CharField(max_length=500)),
                ('died', models.CharField(max_length=500)),
                ('titles', models.CharField(max_length=500)),
                ('aliases', models.CharField(max_length=500)),
                ('father', models.CharField(max_length=500)),
                ('mother', models.CharField(max_length=500)),
                ('spouse', models.CharField(max_length=500)),
                ('allegiances', models.CharField(max_length=500)),
                ('povBooks', models.CharField(max_length=500)),
                ('tvSeries', models.CharField(max_length=500)),
                ('playedBy', models.CharField(max_length=500)),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters_associated', to='app1.books1')),
            ],
        ),
    ]
