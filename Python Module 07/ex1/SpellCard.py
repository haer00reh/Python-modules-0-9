from typing import Dict, List, Any, Union
from ex0.Card import Card


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {'card_played': game_state['name'], 'mana_used': 3,
                'effect': 'Deal 3 damage to target'}

    def get_card_info(self) -> Dict[str, Any]:
        return {'name': self.name, 'cost': self.cost,
                'rarity': self.rarity, 'effect': self.effect_type}

    def resolve_effect(self, targets: List[Dict[str, Any]]) -> \
            Union[str, Dict[str, Any]]:
        if not targets:
            return "No targets"

        target = targets[0]

        if self.effect_type == "damage":
            target["hp"] -= self.value
            return f"Deal {self.value} damage to {target['name']}"

        elif self.effect_type == "heal":
            target["hp"] += self.value
            return f"Heal {target['name']} for {self.value}"

        elif self.effect_type == "buff":
            target["buff"] = {
                "value": self.value,
                "duration": self.duration
            }
            msg = f"Buff {target['name']} for {self.value} "
            msg += f"({self.duration} turns)"
            return msg

        elif self.effect_type == "debuff":
            target["debuff"] = {
                "value": self.value,
                "duration": self.duration
            }
            msg = f"Debuff {target['name']} for {self.value} "
            msg += f"({self.duration} turns)"
            return msg
        else:
            return {}
