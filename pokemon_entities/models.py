from django.db import models


class Pokemon(models.Model):
    title = models.TextField(max_length=200, verbose_name='Pokemon')
    image = models.ImageField(upload_to='pokemons', null=True)

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.DO_NOTHING, verbose_name='Покемон')
    appeared_at = models.DateTimeField(verbose_name='Момент появления', blank=True)
    disappeared_at = models.DateTimeField(verbose_name='Момент исчезновения', blank=True)
    level = models.IntegerField(verbose_name='Уровень', default=0)
    health = models.IntegerField(verbose_name='Здоровье', default=0)
    strength = models.IntegerField(verbose_name='Сила', default=0)
    defence = models.IntegerField(verbose_name='Защита', default=0)
    stamina = models.IntegerField(verbose_name='Выносливость', default=0)
