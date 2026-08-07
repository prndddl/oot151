import json
from pathlib import Path
import requests
import time

CACHE_DIR = 'data/pokeapi/pokemon'
BASE_URL = 'https://pokeapi.co/api/v2'

def fetch_pokemon(pokemon_id: int):
    cache_path = f'{CACHE_DIR}/{pokemon_id}.json'

    Path(CACHE_DIR).mkdir(parents=True, exist_ok=True)
    if Path(cache_path).exists():
        with open(cache_path, 'r') as f:
            print(f'Loading cached data for Pokemon ID {pokemon_id} from {cache_path}')
            return json.load(f)

    pokemon_url = f'{BASE_URL}/pokemon/{pokemon_id}'
    species_url = f'{BASE_URL}/pokemon-species/{pokemon_id}'

    pokemon = requests.get(pokemon_url).json()
    species = requests.get(species_url).json()

    data = {
        "pokemon": pokemon,
        "species": species
    }

    with open(cache_path, 'w') as f:
        json.dump(data, f, indent=2)
        print(f'Cached data for Pokemon ID {pokemon_id} at {cache_path}')

    return data

def fetch_generation_one():
    for i in range(1, 152):
        fetch_pokemon(i)

if __name__ == '__main__':
    fetch_generation_one()
    

        