from typing import List, Dict, Any, Optional
from ex0.Card import Card
import random


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        try:
            self.cards.remove(card_name)
        except (ValueError, AttributeError) as e:
            print(f"Error removing card: {e}")
            return False

    def shuffle(self) -> None:
        try:
            random.shuffle(self.cards)
        except Exception as e:
            print(f"Error shuffling deck: {e}")

    def draw_card(self) -> Optional[Card]:
        try:
            if self.cards:
                card_name = self.cards[0].name
                card_class = self.cards[0].__class__.__name__
                print(f"drew: {card_name} ({card_class})")
                return self.cards.pop(0)
            return None
        except (IndexError, AttributeError) as e:
            print(f"Error drawing card: {e}")
            return None

    def get_deck_stats(self) -> Dict[str, Any]:
        try:
            stats = {
                "total_cards": len(self.cards),
                "creatures": 0,
                "spells": 0,
                "artifacts": 0,
                "avg_cost": 0.0
            }
            total_cost = 0

            for card in self.cards:
                total_cost += getattr(card, "cost", 0)
                if card.__class__.__name__ == "SpellCard":
                    stats["spells"] += 1
                elif card.__class__.__name__ == "ArtifactCard":
                    stats["artifacts"] += 1
                elif card.__class__.__name__ == "CreatureCard":
                    stats["creatures"] += 1

            if self.cards:
                stats["avg_cost"] = int(total_cost / len(self.cards))

            return stats
        except Exception as e:
            print(f"Error getting deck stats: {e}")
            return {"error": str(e)}
