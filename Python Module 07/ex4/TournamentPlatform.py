from typing import Dict, List, Any
from ex4.TournamentCard import TournamentCard
import random


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: Dict[str, TournamentCard] = {}
        self.matches: List[Dict[str, Any]] = []
        self.leaderboard: List[Dict[str, Any]] = []

    def register_card(self, card: TournamentCard) -> None:
        self.cards[card.id] = card

    def create_match(self, card1_id: str,
                     card2_id: str) -> Dict[str, Any]:
        card1 = self.cards.get(card1_id)
        card2 = self.cards.get(card2_id)

        if not card1 or not card2:
            msg = "Both cards must be registered in the platform."
            raise ValueError(msg)

        winner = random.choice([card1, card2])
        loser = card2 if winner == card1 else card1

        winner.update_wins(winner.wins + 1)
        loser.update_losses(loser.losses + 1)
        self.leaderboard.append({
            'card': winner.name,
            'rating': winner.calculate_rating(),
            'rank': winner.get_rank_info()
        })

        return {
            'winner': winner.name,
            'loser': loser.name,
            'winner_rating': winner.calculate_rating(),
            'loser_rating': loser.calculate_rating()
        }

    def get_leaderboard(self) -> List[Dict[str, Any]]:
        return self.leaderboard

    def generate_tournament_report(self) -> Dict[str, Any]:
        total = len(self.cards)
        avg = sum(card.calculate_rating()
                  for card in self.cards.values()) / total
        return {
            "total_cards": total,
            "total_matches": len(self.matches),
            "average_rating": avg,
            "platform_status": "active"
        }
