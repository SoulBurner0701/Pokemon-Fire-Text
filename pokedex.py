# IMPORT
import pickle

from requests.models import HTTPError
import common
import consts
import requests
from common import capital, log

# FUNCTIONS
# def check_pokemon(data, pokemon):
    # for i in range(len(data)):
    #     poke_data = data[i]

    #     # checking if pokemon exists
    #     if poke_data["name"].lower() == pokemon:

    #         # printing data about the pokemon
    #         common.deco("ID: " + str(i), bottom=False)
    #         for key, value in poke_data.items():

    #             # if the key is a list, convert it into a string
    #             if type(value) == list:
    #                value = ", ".join(value)

    #             print(common.capital(key) + ": ", value)
    #         break
    # else:
    #     print("Pokemon not found...")
    # data = common.api_data(consts.POKEMON_URL)["results"]
    # for i in range(len(data)):
    #     poke_dict = data[i]
    #     name = poke_dict["name"]

    #     if name.lower() == pokemon:
    #         print(f"ID: {i+1}")
    #         print(f"Name: {common.capital(name)}")
    #         url = poke_dict["url"]
    #         poke_data = common.api_data(url)


def get_poke_type(name:str) -> list:
    """Returns the type of the given pokemon

    Args:
        name: name of the pokemon
    Returns:
        types: list of the types
    """
    url = consts.POKEMON_URL + name
    data = common.api_data(url)
    
    types = []
    for poke_type in data["types"]:
        types.append(poke_type["type"])
    return types


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
####

print(get_poke_weakness("bulbasaur"))


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
