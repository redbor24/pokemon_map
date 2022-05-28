from django.db import models


class Pokemon(models.Model):
    title = models.TextField(max_length=200, verbose_name='Pokemon')
    image = models.ImageField(upload_to='pokemons', null=True)

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.DO_NOTHING)
