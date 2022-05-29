from django.contrib import admin

from pokemon_entities.models import Pokemon, PokemonEntity


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_ru', 'description')


@admin.register(PokemonEntity)
class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = ('pokemon', 'lat', 'lon', 'appeared_at', 'disappeared_at',
                    'level', 'health', 'strength', 'defence', 'stamina')

