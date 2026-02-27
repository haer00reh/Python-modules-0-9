from typing import Dict, Any, Optional
from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        pass

    def get_card_info(self) -> Optional[Dict[str, Any]]:
        pass

    def is_playable(self, available_mana: int) -> bool:
        try:
            if available_mana < 5:
                return False
            else:
                return True
        except (TypeError, ValueError) as e:
            print(f"Error checking playability: {e}")
            return False
