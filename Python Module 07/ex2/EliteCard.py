from typing import Dict, List, Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Combatable, Card, Magical):
    def __init__(self, name: str, cost: int, rarity: str, effect: str,
                 health: int, damage: int, mana: int) -> None:
        super().__init__(name, cost, rarity)
        self.effect = effect
        self.health = health
        self.damage = damage
        self.mana = mana

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        try:
            return {'card_played': game_state['name'],
                    'mana_used': 5, 'effect': f'{self.effect}'}
        except KeyError as e:
            print(f"Error playing card: Missing key {e}")
            return {'error': 'Invalid game state'}

    def get_card_info(self) -> Dict[str, Any]:
        return {'name': self.name, 'cost': self.cost,
                'rarity': self.rarity, 'type': 'Creature',
                'attack': self.attack, 'health': self.health}

    def is_playable(self, available_mana: int) -> bool:
        try:
            if available_mana < 5:
                return False
            else:
                return True
        except (TypeError, ValueError) as e:
            print(f"Error checking playability: {e}")
            return False

    def attack(self, target: str) -> Dict[str, Any]:
        return {'attacker': f'{self.name}', 'target': f'{target}',
                'damage': 5, 'combat_type': 'melee'}

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        try:
            if incoming_damage < self.health + 3:
                return {'defender': f'{self.name}',
                        'damage_taken': incoming_damage,
                        'damage_blocked': 3, 'still_alive': True}
            else:
                return {'defender': f'{self.name}',
                        'damage_taken': incoming_damage,
                        'damage_blocked': 3, 'still_alive': False}
        except (TypeError, AttributeError) as e:
            print(f"Error defending: {e}")
            return {'error': str(e)}

    def get_combat_stats(self) -> Dict[str, int]:
        return {'attack damage': self.damage, 'defense': 3}

    def cast_spell(self, spell_name: str,
                   targets: List[str]) -> Dict[str, Any]:
        try:
            self.mana -= 4
            return {'caster': self.name, 'spell': spell_name,
                    'targets': targets, 'mana_used': 4}
        except (TypeError, AttributeError) as e:
            print(f"Error casting spell: {e}")
            return {'error': str(e)}

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        try:
            self.mana += amount
            return {'channeled': amount, 'total_mana': self.mana}
        except (TypeError, AttributeError) as e:
            print(f"Error channeling mana: {e}")
            return {'error': str(e)}

    def get_magic_stats(self) -> Dict[str, Any]:
        return {'caster': self.name, 'totat_mana': self.mana}
