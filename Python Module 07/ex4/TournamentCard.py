from typing import Dict, Any
from ex2.Combatable import Combatable
from ex0.Card import Card
from ex4.Rankable import Rankable


class TournamentCard(Combatable, Card, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, damage: int,
                 health: int, combat_type: str, id: str,
                 rating: int) -> None:
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.health = health
        self.combat_type = combat_type
        self.rating = rating
        self.wins = 0
        self.losses = 0
        self.rank = "Unranked"
        self.record = "0-0"
        self.id = id

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {'card_played': game_state['name'], 'mana_used': 3,
                'effect': game_state['effect']}

    def calculate_rating(self) -> int:
        return self.wins * 10 - self.losses * 5

    def update_wins(self, wins: int) -> None:
        self.wins = wins
        self.rating += wins * 10

    def update_losses(self, losses: int) -> None:
        self.losses = losses
        self.rating -= losses * 5

    def get_rank_info(self) -> Dict[str, Any]:
        return self.rank

    def attack(self, target: str) -> Dict[str, Any]:
        return {'attacker': f'{self.name}', 'target': f'{target}',
                'damage': self.damage, 'combat_type': self.combat_type}

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        if incoming_damage < self.health + 3:
            return {'defender': f'{self.name}',
                    'damage_taken': incoming_damage,
                    'damage_blocked': 3, 'still_alive': True}
        else:
            return {'defender': f'{self.name}',
                    'damage_taken': incoming_damage,
                    'damage_blocked': 3, 'still_alive': False}

    def get_combat_stats(self) -> Dict[str, int]:
        return {'attack damage': self.damage, 'defense': self.health}

    def get_tournament_stats(self) -> Dict[str, Any]:
        return {'wins': self.wins, 'losses': self.losses,
                'rating': self.calculate_rating(), 'rank': self.rank}
