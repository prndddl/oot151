import csv
import json
from pathlib import Path
from typing import Any

from fetch_pokemon import fetch_pokemon
from fetch_evolution_chains import fetch_evolution_chain

CACHE_DIR = 'data/pokeapi/pokemon'
CHAIN_CACHE_DIR = 'data/pokeapi/evolution-chain'
OUTPUT_CSV = 'data/pokemon_data.csv'

STAT_NAMES = [
    'hp',
    'attack',
    'defense',
    'special-attack',
    'special-defense',
    'speed'
]

CSV_COLUMNS = [
    'id',
    'name',
    'type1',
    'type2',
    'evolution_stage',
    'total_stats'
] + STAT_NAMES

def parse_pokemon(data: dict[str, Any]) -> dict[str, str]:

    p = data['pokemon']
    s = data['species']

    stats = {entry['stat']['name']: entry['base_stat'] for entry in p['stats']}
    types = [t['type']['name'] for t in sorted(p['types'], key=lambda x: x['slot'])]

    chain = int(s['evolution_chain']['url'].rstrip('/').split('/')[-1])
    data = fetch_evolution_chain(chain)
    stage = search_evolution_stage(data['chain'], p['name'])

    return {
        "id": str(p['id']),
        "name": str(p['name']),
        "type1": str(types[0]),
        "type2": str(types[1]) if len(types) > 1 else '',
        "evolution_stage": str(stage),
        "total_stats": str(sum(stats.values())),
        **{k: str(v) for k, v in stats.items()},
        
    }

def search_evolution_stage(chain: dict, pokemon_name: str, stage: int=1) -> int:
    if chain['species']['name'] == pokemon_name:
        return stage

    stage += 0 if chain.get('is_baby', False) else 1
    for next_chain in chain.get('evolves_to', []):        
        result = search_evolution_stage(next_chain, pokemon_name, stage)
        if result != -1:
            return result

    # If we reach here, the pokemon is not in this chain    
    return -1

def generate_csv():
    pokemon = []
    for i in range(1, 152):
        parsed = parse_pokemon(fetch_pokemon(i))
        pokemon.append(parsed)

    with open(OUTPUT_CSV, 'w', newline='') as f:
        f.truncate(0)
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(pokemon)

if __name__ == '__main__':
    generate_csv()