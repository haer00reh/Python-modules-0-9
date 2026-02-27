from typing import Dict, List, Optional, Union, Tuple
import random
from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.Card import Card


class FantasyCardFactory(CardFactory):

    def __init__(self) -> None:
        self.creatures: Dict[str, Tuple[str, int, str, int, int]] = {
            "dragon": ("Fire Dragon", 5, 'Legendary', 5, 8),
            "goblin": ("Goblin Warrior", 2, 'Common', 2, 3)
        }

        self.spells: Dict[str, Tuple[str, int, str, str]] = {
            "fireball": ("Fireball", 3, 'Common', 'Damage'),
            "lightning": ("Lightning Bolt", 3, 'Epic', 'Damage')
        }

        self.artifacts: Dict[str, Tuple[str, int, str, int, str]] = {
            "mana_ring": ("Mana Ring", 1, "Uncommon", 3, 'Regen')
        }

    def create_creature(self,
                        name_or_power: Optional[Union[str, int]] = None
                        ) -> CreatureCard:
        try:
            if isinstance(
                    name_or_power, str) and name_or_power in self.creatures:
                key = name_or_power
            else:
                key = random.choice(list(self.creatures.keys()))

            name, cost, rarity, attack, health = self.creatures[key]
            return CreatureCard(name, cost, rarity, attack, health)
        except (KeyError, ValueError) as e:
            print(f"Error creating creature: {e}")
            # Return a default creature card
            return CreatureCard("Default Creature", 1, "Common", 1, 1)

    def create_spell(self,
                     name_or_power: Optional[Union[str, int]] = None
                     ) -> SpellCard:
        try:
            key = name_or_power if isinstance(name_or_power, str) else \
                random.choice(list(self.spells.keys()))
            name, cost, rarity, effect_type = self.spells[key]
            return SpellCard(name, cost, rarity, effect_type)
        except (KeyError, ValueError) as e:
            print(f"Error creating spell: {e}")
            return SpellCard("Default Spell", 1, "Common", "Damage")

    def create_artifact(self,
                        name_or_power: Optional[Union[str, int]] = None
                        ) -> ArtifactCard:
        try:
            key = name_or_power if isinstance(name_or_power, str) else \
                random.choice(list(self.artifacts.keys()))
            name, cost, rarity, durability, effect = self.artifacts[key]
            return ArtifactCard(name, cost, rarity, durability, effect)
        except (KeyError, ValueError) as e:
            print(f"Error creating artifact: {e}")
            return ArtifactCard("Default Artifact", 1, "Common", 1, "None")

    def create_themed_deck(self, size: int) -> List[Card]:
        try:
            deck = []
            for _ in range(size):
                choice = random.choice(["creature", "spell", "artifact"])

                if choice == "creature":
                    deck.append(self.create_creature())
                elif choice == "spell":
                    deck.append(self.create_spell())
                else:
                    deck.append(self.create_artifact())

            return deck
        except Exception as e:
            print(f"Error creating themed deck: {e}")
            return []

    def get_supported_types(self) -> Dict[str, List[str]]:
        return {
            "creatures": list(self.creatures.keys()),
            "spells": list(self.spells.keys()),
            "artifacts": list(self.artifacts.keys())
        }
