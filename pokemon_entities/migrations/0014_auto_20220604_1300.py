# Generated by Django 3.1.14 on 2022-06-04 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0013_auto_20220604_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enitites', to='pokemon_entities.pokemon', verbose_name='Покемон'),
        ),
    ]