from django.db import models


class Pokemon(models.Model):
    title = models.TextField(max_length=200, verbose_name='Pokemon')
    image = models.ImageField(upload_to='pokemons', null=True)
