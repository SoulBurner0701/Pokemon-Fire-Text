# IMPORT
import pickle

from requests.models import HTTPError
import common
import consts
import requests
from common import capital, log


def get_poke_type(name:str) -> list:
    """Returns the type of the given pokemon

    Args:
        name: name of the pokemon
    Returns:
        types: list of the types
    """
    url = consts.POKEMON_URL + name
    data = common.api_data(url)["types"]
    
    return [poke_type["type"] for poke_type in data]


def get_poke_weakness(name:str) -> list:
    """Returns the weaknesses of a pokemon
    
    Args:
        name: name of the pokemon
    Returns:
        weaknesses: list of the weaknesses of the pokemon
    """

    # getting the type of the pokemon
    types = get_poke_type(name)
    weaknesses = []
    # [{"name": "flying", "url": "asdf.com"}, {}, {}]
    # appending all possible weaknesses to the list
    for poke_type in types:
        url = poke_type["url"]
        data = common.api_data(url)["damage_relations"]

        for weakness in data["double_damage_from"]:
            if weakness not in weaknesses:
                weaknesses.append(weakness)

    # removing wrong weaknesses
    for poke_type in types:
        url = poke_type["url"]
        data = common.api_data(url)["damage_relations"]
        to_remove = ["double_damage_to", "half_damage_from", "no_damage_from"]
        for key in to_remove:
            for weakness in data[key]:
                if weakness in weaknesses:
                    weaknesses.remove(weakness)
    return weaknesses


def get_abilities(name: str) -> list:
    url = consts.POKEMON_URL + name
    data = common.api_data(url)["abilities"]

    return [ability["ability"] for ability in data]



def search():
    # printing figlet for style 😎
    common.deco(consts.figlet_pokedex)

    while True:
        # getting user input
        pokemon = common.user_input("search Pokemon (q to quit)").lower()

        # getting data
        data = common.read_bin(consts.FILE_POKEDEX)

        # checking for pokemon 
        if pokemon == "q":
            break
        else:
            # check_pokemon(data, pokemon)
            common.deco("", top=False)
