from typing import Dict, Any
from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        try:
            return {'card_played': {game_state['name']},
                    'mana_used': 3, 'effect': self.effect}
        except KeyError as e:
            print(f"Error playing artifact: Missing key {e}")
            return {'error': 'Invalid game state'}

    def get_card_info(self) -> Dict[str, Any]:
        return {'name': self.name, 'cost': self.cost,
                'rarity': self.rarity, 'effect': self.effect}

    def activate_ability(self) -> Dict[str, str]:
        return {"artifact_activated": self.name}
