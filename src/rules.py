from pokemon import Pokemon
from categories import pokemon_categories

# Hierarchy of rules to apply to templates
# Applied in descending order, with later rules overriding earlier rules
# TYPE -> STAT -> EVOLUTION -> CATEGORY -> INDIVIDUAL


# We apply secondary type (if present) first, then primary type
TYPE_RULES = {
    "normal": {
        "door_of_time": { "closed": 50, "song_only": 0,"open": 0},
        "starting_age": {"child": 50, "adult": 0},

    },
    "fire": {
        "kakariko_gate": {"closed": 0, "open": 50},
        "shuffle_beehives": { "false": 0, "true": 50},
        "shuffle_pots": { "off": 0, "dungeon": 50, "overworld": 0, "all": 0},
        "shuffle_trees": { "false": 0, "true": 50},
    },
    "water": {
        "zoras_fountain": {"closed": 0, "closed_as_child": 0, "open": 50},
        "sleeping_waterfall": { "closed": 0, "open": 50},
        "jabu_jabu": {"closed": 0, "open": 50},
        "shuffle_swim": {"false": 50, "true": 0},
        "shuffle_fish": { "off": 0, "pond": 50, "overworld": 0, "all": 0},
        "shuffle_grass":  { "off": 0, "dungeon": 0, "overworld": 0, "all": 50},
    },
    "electric": {
        "shuffle_scrubs": {
            "off": 0,
            "one_time_only": 0,
            "all": 50
        },
    },
    "grass": {
        "closed_forest": {"on": 50, "deku_only": 0, "off": 0},
        "shuffle_scrubs": {
            "off": 0,
            "one_time_only": 0,
            "all": 50
        },
        "shuffle_crates": { "off": 0, "dungeon": 50, "overworld": 0, "all": 0},
        "shuffle_trees": { "false": 0, "true": 50},
        "shuffle_grass":  { "off": 0, "dungeon": 0, "overworld": 0, "all": 50},
    },
    "ice": {
        "zoras_fountain": {"closed": 0, "closed_as_child": 0, "open": 50},
        "sleeping_waterfall": { "closed": 0, "open": 50},
        "jabu_jabu": {"closed": 0, "open": 50},
        "shuffle_fish": { "off": 0, "pond": 50, "overworld": 0, "all": 0},
        "ice_trap_count": {
            20: 50,
            "random": 0,
            "random-low": 0,
            "random-high": 0,
            "random-range-0-100": 0
        },
    },
    "fighting": {
        "shuffle_crates": { "off": 0, "dungeon": 0, "overworld": 50, "all": 0},
    },
    "poison": {
        "closed_forest": {"on": 50, "deku_only": 0, "off": 0},
        "shuffle_beehives": {"false": 0, "true": 50},
    },
    "ground": {
        "kakariko_gate": {"closed": 0, "open": 50},
        "shuffle_pots": { "off": 0, "dungeon": 50, "overworld": 0, "all": 0},
    },
    "flying": {
        "rocs_feather": {"false": 0, "true": 50},
        "shuffle_fish": { "off": 0, "pond": 50, "overworld": 0, "all": 0},
        "shuffle_trees": { "false": 0, "true": 50},
    },
    "psychic": {
        "lock_overworld_doors": { "false": 0, "true": 50},
    },
    "bug": {
        "closed_forest": {"on": 50, "deku_only": 0, "off": 0},
        "shuffle_beehives": { "false": 0, "true": 50},
        "shuffle_grass":  { "off": 0, "dungeon": 0, "overworld": 0, "all": 50},
    },
    "rock": {
        "kakariko_gate": {"closed": 0, "open": 50},
        "shuffle_beehives": { "false": 0, "true": 50},
        "shuffle_pots": { "off": 0, "dungeon": 50, "overworld": 0, "all": 0},
    },
    "ghost": {
        "lock_overworld_doors": { "false": 0, "true": 50},
        "shuffle_crates": { "off": 0, "dungeon": 50, "overworld": 0, "all": 0},
        "shuffle_boss_souls": { "off": 0, "on": 50, "on_plus_ganons": 0},
        "big_poe_target_count": {
            10: 50,
            "random": 0,
            "random-low": 0,
            "random-high": 0,
            "random-range-0-10": 0
        },
        "hint_clarity": {
            "obscure": 0,
            "ambiguous": 50,
            "clear": 0
        }
    },
    "dragon": {
        "shuffle_scrubs": {
            "off": 0,
            "one_time_only": 0,
            "all": 50
        },
        "shuffle_boss_souls": { "off": 0, "on": 50, "on_plus_ganons": 0},
    },
    "fairy": {
        "shuffle_fountain_fairies": { "false": 0, "true": 50},
        "shuffle_stone_fairies": { "false": 0, "true": 50},
        "shuffle_bean_fairies": { "false": 0, "true": 50},
        "shuffle_song_fairies": { "false": 0, "true": 50},
    },
    "steel": {

    }
}

EVOLUTION_RULES = {
    "1": {
        "shuffle_freestanding_items": {
            "off": 50,
            "dungeon": 0,
            "overworld": 0,
            "all": 0
        },
        "shuffle_kokiri_sword": {
            "false": 50,
            "true": 0
        },
        "shuffle_shops_minimum_price": {
            10: 50,
            "random": 0,
            "random-low": 0,
            "random-high": 0,
            "random-range-0-999": 0
        },
        "shuffle_shops_maximum_price": {
            99: 50,
            "random": 0,
            "random-low": 0,
            "random-high": 0,
            "random-range-0-999": 0
        },
        "small_key_shuffle": {
            "start_with": 0,
            "vanilla": 0,
            "own_dungeon": 50,
            "any_dungeon": 0,
            "overworld": 0,
            "anywhere": 0
        },
        "boss_key_shuffle": {
            "start_with": 0,
            "vanilla": 0,
            "own_dungeon": 50,
            "any_dungeon": 0,
            "overworld": 0,
            "anywhere": 0
        },
        "item_pool": {
            "balanced": 0,
            "plentiful": 50,
            "scarce": 0,
            "minimal": 0
        }
    },
    "2": {
        "shuffle_freestanding_items": {
            "off": 0,
            "dungeon": 50,
            "overworld": 0,
            "all": 0
        },
        "shuffle_master_sword": {
            "false": 0,
            "true": 50
        },
        "shuffle_shops_minimum_price": {
            25: 50,
            "random": 0,
            "random-low": 0,
            "random-high": 0,
            "random-range-0-999": 0
        },
        "shuffle_shops_maximum_price": {
            199: 50,
            "random": 0,
            "random-low": 0,
            "random-high": 0,
            "random-range-0-999": 0
        },
        "small_key_shuffle": {
            "start_with": 0,
            "vanilla": 0,
            "own_dungeon": 0,
            "any_dungeon": 50,
            "overworld": 0,
            "anywhere": 0
        },
        "boss_key_shuffle": {
            "start_with": 0,
            "vanilla": 0,
            "own_dungeon": 0,
            "any_dungeon": 50,
            "overworld": 0,
            "anywhere": 0
        },
        "item_pool": {
            "balanced": 50,
            "plentiful": 0,
            "scarce": 0,
            "minimal": 0
        },
    },
    "3": {
        "shuffle_freestanding_items": {
            "off": 0,
            "dungeon": 0,
            "overworld": 50,
            "all": 0
        },
        "shuffle_shops_minimum_price": {
            50: 50,
            "random": 0,
            "random-low": 0,
            "random-high": 0,
            "random-range-0-999": 0
        },
        "shuffle_shops_maximum_price": {
            299: 50,
            "random": 0,
            "random-low": 0,
            "random-high": 0,
            "random-range-0-999": 0
        },
        "small_key_shuffle": {
            "start_with": 0,
            "vanilla": 0,
            "own_dungeon": 0,
            "any_dungeon": 0,
            "overworld": 50,
            "anywhere": 0
        },
        "boss_key_shuffle": {
            "start_with": 0,
            "vanilla": 0,
            "own_dungeon": 0,
            "any_dungeon": 0,
            "overworld": 50,
            "anywhere": 0
        },
        "item_pool": {
            "balanced": 0,
            "plentiful": 0,
            "scarce": 50,
            "minimal": 0
        },
    },
}

# Custom categories from categories.json
CATEGORY_RULES = {
    "fossil": {
        "rainbow_bridge": {
            "vanilla": 0,
            "always_open": 0,
            "stones": 0,
            "medallions": 0,
            "dungeon_rewards": 0,
            "dungeons": 0,
            "tokens": 50,
            "greg": 0
        },
        "skeleton_key": {
            "false": 0,
            "true": 50
        },
    },
    "legendary": {
        "ganons_trials_count": {
                6: 50,
                "random": 0,
                "random-low": 0, 
                "random-high": 0, 
                "random-range-0-6": 0
        },
        "shuffle_freestanding_items": {
            "off": 0,
            "dungeon": 0,
            "overworld": 0,
            "all": 50
        },
        "shuffle_shops_minimum_price": {
            75: 50,
            "random": 0,
            "random-low": 0,
            "random-high": 0,
            "random-range-0-999": 0
        },
        "shuffle_shops_maximum_price": {
            499: 50,
            "random": 0,
            "random-low": 0,
            "random-high": 0,
            "random-range-0-999": 0
        },
        "shuffle_pots": { "off": 0, "dungeon": 0, "overworld": 0, "all": 50},
        "shuffle_crates": { "off": 0, "dungeon": 0, "overworld": 0, "all": 50},
        "shuffle_trees": { "false": 0, "true": 50},
        "shuffle_boss_souls": { "off": 0, "on": 50, "on_plus_ganons": 0},
        "small_key_shuffle": {
            "start_with": 0,
            "vanilla": 0,
            "own_dungeon": 0,
            "any_dungeon": 0,
            "overworld": 0,
            "anywhere": 50
        },
        "boss_key_shuffle": {
            "start_with": 0,
            "vanilla": 0,
            "own_dungeon": 0,
            "any_dungeon": 0,
            "overworld": 0,
            "anywhere": 50
        },
        "item_pool": {
            "balanced": 0,
            "plentiful": 0,
            "scarce": 50,
            "minimal": 0
        },

    },
    "safari": {
        "triforce_hunt": {
            "false": 0,
            "true": 50
        },
    },
}

INDIVIDUAL_RULES = {
    "jigglypuff": {
        "shuffle_songs": {
            "off": 0,
            "song_locations": 0,
            "dungeon_rewards": 50,
            "anywhere": 0
        },
        "shuffle_ocarina_buttons": {
            "false": 0,
            "true": 50
        },
        "start_with_ocarina": {
            "off": 0,
            "fairy_ocarina": 50,
            "ocarina_of_time": 0
        },
    },
    "magikarp": {
        "shuffle_fishing_pole": {
            "true": 50,
            "false": 0
        },
    },
    "meowth": {
        "shuffle_childs_wallet": {
            "false": 0,
            "true": 50
        },
        "shuffle_tycoon_wallet": {
            "false": 50,
            "true": 0  
        }
    },
    "persian": {
        "shuffle_childs_wallet": {
            "false": 0,
            "true": 50
        },
        "shuffle_tycoon_wallet": {
            "false": 50,
            "true": 0  
        }
    },
    "tauros": {
        "shuffle_cows": {
            "false": 0,
            "true": 50
        },
    },
}

def get_rules(pokemon: Pokemon):
    rules = {}

    if (pokemon.type2 != ''):
        rules = add_type_rules(pokemon.type2, rules)
    rules = add_type_rules(pokemon.type1, rules)

    rules = add_stat_rules(pokemon, rules)
    rules = add_evolution_rules(pokemon.evolution_stage, rules)
    rules = add_category_rules(pokemon.name, rules)
    rules = add_individual_rules(pokemon.name, rules)
    return rules

def add_type_rules(pokemon_type, rules) -> dict:
    for type_rule, rule_settings in TYPE_RULES.get(pokemon_type, {}).items():
        if type_rule not in rules:
            rules[type_rule] = {}
        rules[type_rule].update(rule_settings)
    return rules

def add_stat_rules(pokemon, rules) -> dict:
    total = pokemon.total_stats

    progression = -1/7*total+100
    progression = max(0, min(progression, 99))

    rules["progression_balancing"] = { 
        "random": 0,
        "random-low": 0,
        "random-high": 0,
        "random-range-0-99": 0,
        "disabled": 0,
        "normal": 0,
        "extreme": 0,
        round(progression): 50
    }
    return rules

def add_evolution_rules(evolution_stage, rules) -> dict:
    for type_rule, rule_settings in EVOLUTION_RULES.get(str(evolution_stage), {}).items():
        rules[type_rule] = rule_settings
    return rules

def add_category_rules(pokemon_name, rules) -> dict:
    for category_name, category in pokemon_categories.items():
        if pokemon_name not in category:
            continue

        rule_settings = CATEGORY_RULES.get(category_name, {})
        for type_rule, rule_setting in rule_settings.items():
            rules[type_rule] = rule_setting

    return rules

def add_individual_rules(pokemon_name, rules) -> dict:
    if pokemon_name not in INDIVIDUAL_RULES:
        return rules

    rule_settings = INDIVIDUAL_RULES[pokemon_name]
    for type_rule, rule_settings in rule_settings.items():
        rules[type_rule] = rule_settings
    return rules