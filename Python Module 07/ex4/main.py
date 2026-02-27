from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


print("\n=== DataDeck Tournament Platform ===\n")

print("Registering Tournament Cards...\n")
card1 = TournamentCard(
    "Flame Dragon", 5, "Epic", 8, 5, "Fire",
    "dragon_001", 1200)
card2 = TournamentCard(
    "Ice Wizard", 4, "Rare", 5, 8, "Ice",
    "wizard_002", 1150)

print(f"Fire Dragon (ID: {card1.id}):")
print("- Interfaces: [Card, Combatable, Rankable]")
print(f"- Rating: {card1.rating}")
print("- Record: 0-0\n")

print(f"Ice Wizard (ID: {card2.id}):")
print("- Interfaces: [Card, Combatable, Rankable]")
print(f"- Rating: {card2.rating}")
print("- Record: 0-0\n")

print("Creating tournament match...")
platform = TournamentPlatform()
platform.register_card(card1)
platform.register_card(card2)
match = platform.create_match(card1.id, card2.id)
print(f"Match result: {match}")
print("\nTournament Leaderboard:")
print(f"1. {match['winner']} - Rating: {match['winner_rating']} (1-0)")
print(f"2. {match['loser']} - Rating: {match['loser_rating']} (0-1)\n")
print(f"Platform Report: \n{platform.generate_tournament_report()}\n")

print("=== Tournament Platform Successfully Deployed! ===")
print("All abstract patterns working together harmoniously!")
