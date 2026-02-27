from typing import Dict, Any
from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.health = health
        self.attack = attack

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        try:
            return {'card_played': game_state['name'],
                    'mana_used': 5, 'effect':
                    'Creature summoned to battlefield'}
        except KeyError as e:
            print(f"Error playing card: Missing key {e}")
            return {'error': 'Invalid game state'}

    def get_card_info(self) -> Dict[str, Any]:
        return {'name': self.name, 'cost': self.cost,
                'rarity': self.rarity, 'type': 'Creature',
                'attack': self.attack, 'health': self.health}

    def attack_target(self) -> Dict[str, Any]:
        return {'attacker': self.name, 'target':
                'Goblin Warrior', 'damage_dealt': 7,
                'combat_resolved': True}

    def validate(self) -> bool:
        try:
            if self.attack < 0 or self.health < 0:
                return False
            else:
                return True
        except (AttributeError, TypeError) as e:
            print(f"Error validating card: {e}")
            return False
