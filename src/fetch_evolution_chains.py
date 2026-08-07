import json
from pathlib import Path
import requests
import time

CACHE_DIR = 'data/pokeapi/evolution-chain'
BASE_URL = 'https://pokeapi.co/api/v2'

def fetch_evolution_chain(evolution_chain: int):
    Path(CACHE_DIR).mkdir(parents=True, exist_ok=True)
    cache_path = f'{CACHE_DIR}/{evolution_chain}.json'

    if Path(cache_path).exists():
        with open(cache_path, 'r') as f:
            print(f'Loading cached data for Evolution Chain ID {evolution_chain} from {cache_path}')
            return json.load(f)

    url = f'{BASE_URL}/evolution-chain/{evolution_chain}'
    data = requests.get(url).json()

    with open(cache_path, 'w') as f:
        json.dump(data, f, indent=2)
        print(f'Cached data for Evolution Chain ID {evolution_chain} at {cache_path}')
        
    return data

def fetch_generation_one():
    for i in range(1, 79): # Mew is 78
        fetch_evolution_chain(i)

if __name__ == '__main__':
    fetch_generation_one()
    

        