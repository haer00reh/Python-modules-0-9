from typing import Dict, List, Any


class AggressiveStrategy:

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List[str]) -> List[str]:
        try:
            if "Enemy Player" in available_targets:
                result = ["Enemy Player"]
                result += [t for t in available_targets
                           if t != "Enemy Player"]
                return result
            return available_targets
        except (TypeError, AttributeError) as e:
            print(f"Error prioritizing targets: {e}")
            return []

    def execute_turn(self, hand: List[Any],
                     battlefield: Dict[str, List[Any]]) -> Dict[str, Any]:
        try:
            mana_limit = 5
            mana_used = 0

            cards_played = []
            damage_dealt = 0
            targets_attacked = []

            enemy_creatures = battlefield.get("enemy_creatures", [])
            friendly_creatures = battlefield.get("friendly_creatures", [])

            hand_sorted = sorted(hand, key=lambda c: c.cost)

            for card in hand_sorted:
                if mana_used + card.cost > mana_limit:
                    continue

                cards_played.append(card)
                mana_used += card.cost

                if hasattr(card, "attack"):
                    friendly_creatures.append(card)

                    if enemy_creatures:
                        target = enemy_creatures.pop(0)
                        targets_attacked.append(target.name)
                    else:
                        target = "Enemy Player"
                        targets_attacked.append(target)

                    damage_dealt += card.attack

                elif hasattr(card, "damage"):
                    if enemy_creatures:
                        target = enemy_creatures.pop(0)
                        targets_attacked.append(target.name)
                    else:
                        target = "Enemy Player"
                        targets_attacked.append(target)

                    damage_dealt += card.damage

            return {
                "strategy": self.get_strategy_name(),
                "actions": {
                    "cards_played": [c.name for c in cards_played],
                    "mana_used": mana_used,
                    "targets_attacked": targets_attacked,
                    "damage_dealt": damage_dealt
                }
            }
        except Exception as e:
            print(f"Error executing turn: {e}")
            return {
                "strategy": self.get_strategy_name(),
                "actions": {
                    "error": str(e)
                }
            }
