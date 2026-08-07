from dataclasses import dataclass

@dataclass
class Pokemon:
    id: int
    name: str
    type1: str
    type2: str
    evolution_stage: int
    total_stats: int
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int