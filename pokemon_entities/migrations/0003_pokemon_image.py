# Generated by Django 3.1.14 on 2022-05-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_auto_20220527_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(null=True, upload_to='pokemons'),
        ),
    ]
