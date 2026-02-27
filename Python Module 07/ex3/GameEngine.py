from typing import Dict, Optional, Any


class GameEngine:

    def __init__(self) -> None:
        self.factory: Optional[Any] = None
        self.strategy: Optional[Any] = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: Any, strategy: Any) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> None:
        hand = [
            self.factory.create_creature("dragon"),
            self.factory.create_creature("goblin"),
            self.factory.create_spell("lightning")
        ]

        self.cards_created += len(hand)

        battlefield = {
            "enemy_creatures": [],
            "friendly_creatures": []
        }
        hand_str = [f"{card.name} ({card.cost})" for card in hand]
        print(f"Hand: {hand_str}\n")

        result = self.strategy.execute_turn(hand, battlefield)

        print("Turn execution:")
        print(f"Strategy: {result['strategy']}")
        print(f"Actions: {result['actions']}")

        self.total_damage += result["actions"]["damage_dealt"]
        self.turns_simulated += 1

    def get_engine_status(self) -> Dict[str, Any]:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
