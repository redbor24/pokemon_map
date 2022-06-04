import os

import folium
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.http import Http404

from pokemon_entities.models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    current_time = timezone.localtime()
    for pokemon_entity in PokemonEntity.objects.filter(appeared_at__lte=current_time, disappeared_at__gte=current_time):
        if pokemon_entity.pokemon.image:
            add_pokemon(
                folium_map,
                pokemon_entity.lat,
                pokemon_entity.lon,
                request.build_absolute_uri(get_img_url(pokemon_entity.pokemon))
            )
        else:
            add_pokemon(
                folium_map,
                pokemon_entity.lat,
                pokemon_entity.lon
            )

    pokemons_on_page = []
    for pokemon in Pokemon.objects.all():
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': get_img_url(pokemon),
            'title_ru': pokemon.title_ru
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        pokemon = get_object_or_404(Pokemon, id=pokemon_id)
        pokemon_next_evols = []
        try:
            for evol in pokemon.next_evolutions.all():
                pokemon_next_evols.append({
                    'pokemon_id': evol.id,
                    'img_url': get_img_url(evol),
                    'title_ru': evol.title_ru,
                    'title_en': evol.title_en,
                    'title_jp': evol.title_jp,
                    'description': evol.description,
                })
        except ObjectDoesNotExist:
            pass

        if pokemon.previous_evolution:
            pokemon_prev_evol = {
                'pokemon_id': pokemon.previous_evolution.id,
                'img_url': get_img_url(pokemon.previous_evolution),
                'title_ru': pokemon.previous_evolution.title_ru,
                'title_en': pokemon.previous_evolution.title_en,
                'title_jp': pokemon.previous_evolution.title_jp,
                'description': pokemon.previous_evolution.description,
            }
        else:
            pokemon_prev_evol = {}

        requested_pokemon = {
            'pokemon_id': pokemon,
            'img_url': get_img_url(pokemon),
            'title_ru': pokemon.title_ru,
            'title_en': pokemon.title_en,
            'title_jp': pokemon.title_jp,
            'description': pokemon.description,
            'next_evolutions': pokemon_next_evols,
            'previous_evolution': pokemon_prev_evol
        }
    except Http404:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in PokemonEntity.objects.filter(pokemon=pokemon):
        if pokemon_entity.pokemon.image:
            add_pokemon(
                folium_map,
                pokemon_entity.lat,
                pokemon_entity.lon,
                request.build_absolute_uri(get_img_url(pokemon_entity.pokemon))
            )
        else:
            add_pokemon(
                folium_map,
                pokemon_entity.lat,
                pokemon_entity.lon
            )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': requested_pokemon
    })


def get_img_url(pokemon):
    if os.path.isfile(pokemon.image.path):
        return pokemon.image.url
    else:
        return DEFAULT_IMAGE_URL
