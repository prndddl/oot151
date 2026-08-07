from pokemon import Pokemon
from rules import get_rules

from pathlib import Path
import yaml


CUSTOM_TEMPLATE = "data/customTemplate.yaml"
POKEMON_DATA    = "data/pokemon_data.csv"
OUTPUT_DIR     = "output"

YAML_RANGE = range(1, 152)

def generate_yamls():
    pokemon = []
    with open(POKEMON_DATA, 'r') as f:
        for i, line in enumerate(f):
            if i in YAML_RANGE:
                pokemon.append(build_pokemon(line))

    
    for p in pokemon:
        # Reload the template each time
        with open(CUSTOM_TEMPLATE, 'r') as f:
            print(f'Generating YAML for {p.name} (ID: {p.id})')
            generate_yaml(p, f)

def build_pokemon(line: str) -> Pokemon:
    data = line.strip().split(',')
    return Pokemon(
        id=int(data[0]),
        name=data[1],
        type1=data[2],
        type2=data[3],
        evolution_stage=int(data[4]),      
        total_stats=int(data[5]),
        hp=int(data[6]),
        attack=int(data[7]),
        defense=int(data[8]),
        special_attack=int(data[9]),
        special_defense=int(data[10]),
        speed=int(data[11])
    )

def generate_yaml(pokemon: Pokemon, file):
    yaml_data = yaml.safe_load(file)
    # Get rules to apply to the template
    rules = get_rules(pokemon)
    
    for yaml_prop, weightings in rules.items():
        setting = yaml_data["Ship of Harkinian"][yaml_prop]
        for key, weight in weightings.items():
            setting[key] = weight

    # Save the modified YAML
    file_name = f"{pokemon.id:03d}_{pokemon.name}"
    yaml_data["name"] = file_name

    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    with open(f"{OUTPUT_DIR}/{file_name}.yaml", 'w') as f:
        yaml.dump(yaml_data, f)


if __name__ == "__main__":
    generate_yamls()
