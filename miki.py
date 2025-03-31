#---Uppkoppling mot API test---
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data

    else:
        print(f"Failed to retrieve data")

pokemon_name = "charizard"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"]}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")



"""def get_age():

    age = input("Hur gammal är du hehe? ")
    print(f"{age} e riktigt duktig ålder")


def get_food():
    food = input("Vad är din favoritmat ")
    print(f"Ah {food} är riktigt gott!")


def get_drink():
    drink = input("Vad är din favoritdrink ")
    print(f"Ah {drink} är riktigt gott!")"""