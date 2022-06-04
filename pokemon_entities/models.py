from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Имя на русском', blank=True)
    title_en = models.CharField(max_length=200, verbose_name='Имя на английском', blank=True)
    title_jp = models.CharField(max_length=200, verbose_name='Имя на японском', blank=True)
    image = models.ImageField(upload_to='pokemons', null=True)
    description = models.TextField(max_length=1024, verbose_name='Описание', blank=True)
    previous_evolution = models.ForeignKey(
        'Pokemon',
        verbose_name='Предыдущий этап эволюции',
        on_delete=models.DO_NOTHING,
        related_name='next_evolutions',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.id}, {self.title_ru}'


class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name='Покемон',
        related_name='entities'
    )
    appeared_at = models.DateTimeField(verbose_name='Момент появления', blank=True)
    disappeared_at = models.DateTimeField(verbose_name='Момент исчезновения', blank=True)
    level = models.IntegerField(verbose_name='Уровень', default=0)
    health = models.IntegerField(verbose_name='Здоровье', default=0)
    strength = models.IntegerField(verbose_name='Сила', default=0)
    defence = models.IntegerField(verbose_name='Защита', default=0)
    stamina = models.IntegerField(verbose_name='Выносливость', default=0)

    def __str__(self):
        return f'id: {self.id} ({self.pokemon})'
