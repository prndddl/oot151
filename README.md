# oot151

Generates 151 [Archipelago](https://archipelago.gg/) multiworld YAML configuration files for [Ship of Harkinian](https://www.shipofharkinian.com/) (a PC port of The Legend of Zelda: Ocarina of Time) — one file per Generation 1 Pokemon. Each YAML is configured based on the characteristics of its assigned Pokemon: type(s), base stats, evolution stage, and special category membership, so every seed in a multiworld session gets a uniquely themed randomizer experience.

## Requirements

- Python 3
- Internet access (for the initial PokeAPI fetch; subsequent runs use a local cache)

## Usage

Run the full pipeline with the provided script:

**Windows**

```
run.bat
```

The script creates a virtual environment, installs dependencies, and executes steps in order. The 151 output YAML files are written to the `output/` directory.

Individual scripts can also be run on their own (see [Pipeline](#pipeline) below).

## Pipeline

Each step is a standalone Python script in `src/`. Run them in order:

| Step | Script                  | Description                                                                           |
| ---- | ----------------------- | ------------------------------------------------------------------------------------- |
| 1    | `src/generate_csv.py`   | Parses the cached JSON and writes `data/pokemon_data.csv`                             |
| 2    | `src/generate_yamls.py` | Reads the CSV and the base template, applies rules, and writes 151 YAMLs to `output/` |

The fetch scripts skip re-downloading files that already exist, so the PokeAPI is only hit on the first run.

## How Settings Are Determined

Rules are applied in order from lowest to highest priority, with each layer able to override the previous:

1. **Type rules** — The Pokemon's secondary type is applied first, then the primary type. Each type maps to specific YAML settings (e.g., Water type opens Zora's Fountain; Ghost type shuffles boss souls).
2. **Stat formula** — `progression_balancing` is derived from total base stats: higher-stat Pokemon receive lower progression balancing, making their slot harder.
3. **Evolution stage rules** — Stage 1 Pokemon get simpler settings (own-dungeon keys, plentiful items); Stage 3 Pokemon get harder settings (overworld keys, scarce items).
4. **Category rules** — Fossil Pokemon enable rainbow bridge tokens and skeleton key; Legendary Pokemon enable all Ganon's trials and fully shuffle items; Safari Zone Pokemon enable Triforce Hunt.
5. **Individual rules** — Per-Pokemon overrides for specific cases (e.g., Magikarp shuffles the fishing pole; Meowth/Persian shuffle wallets; Jigglypuff shuffles songs and ocarina buttons).

## Project Structure

```
oot151/
├── data/
│   ├── customTemplate.yaml           # Base Archipelago YAML template
│   ├── pokemon_data.csv              # Intermediate data: stats and types for all 151 Pokemon
│   └── pokeapi/                      # Local cache of raw PokeAPI responses (git-ignored)
├── output/                           # Generated YAML files (001_bulbasaur.yaml ... 151_mew.yaml)
├── src/
│   ├── fetch_pokemon.py
│   ├── fetch_evolution_chains.py
│   ├── generate_csv.py
│   ├── generate_yamls.py
│   ├── pokemon.py                    # Pokemon dataclass
│   ├── categories.py                 # Fossil, legendary, and safari Pokemon lists
│   └── rules.py                      # Core logic: maps Pokemon properties to YAML weights
├── run.bat
└── run.sh
```

## Dependencies

Installed automatically by the run scripts:

- [requests](https://pypi.org/project/requests/) — PokeAPI HTTP fetching
- [PyYAML](https://pypi.org/project/PyYAML/) — YAML parsing and generation

## License

See [LICENSE](LICENSE).
