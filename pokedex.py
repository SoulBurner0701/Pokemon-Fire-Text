# IMPORT
import pickle
import functions
import consts
import figlets

# VAR
figlet_length = functions.get_max_length(figlets.figlet_pokedex)

# FUNCTIONS
def check_pokemon(data, pokemon):
    for i in range(len(data)):
        poke_data = data[i]

        # checking if pokemon exists
        if poke_data["name"].lower() == pokemon:

            # printing data about the pokemon
            functions.deco("ID: " + str(i), no_of_dashes=figlet_length, bottom=False)
            for key, value in poke_data.items():

                # if the key is a list, convert it into a string
                if type(value) == list:
                   value = ", ".join(value)

                print(functions.capital(key) + ": ", value)
            break
    else:
        print("Pokemon not found...")


def search():
    # printing figlet for style 😎
    functions.deco(figlets.figlet_pokedex)

    while True:
        # getting user input
        pokemon = functions.user_input("search Pokemon (q to quit)").lower()

        # getting data
        data = functions.read_bin(consts.FILE_POKEDEX)

        # checking for pokemon 
        if pokemon == "q":
            break
        else:
            check_pokemon(data, pokemon)
            functions.deco("", no_of_dashes=figlet_length, top=False)


        


        

        
search()