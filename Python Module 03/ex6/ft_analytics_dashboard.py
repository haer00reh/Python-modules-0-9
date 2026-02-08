players = [
    {
        "name": "alice",
        "score": 2300,
        "achievements": [
            "first_kill",
            "level_10",
            "boss_slayer",
            "treasure_hunter",
            "speed_runner",
        ],
        "region": "north",
    },
    {
        "name": "bob",
        "score": 1800,
        "achievements": ["first_kill", "level_5", "treasure_hunter"],
        "region": "east",
    },
    {
        "name": "charlie",
        "score": 2150,
        "achievements": [
            "level_10",
            "boss_slayer",
            "treasure_hunter",
            "speed_runner",
            "puzzle_master",
            "explorer",
            "sharpshooter",
        ],
        "region": "central",
    },
    {
        "name": "diana",
        "score": 2300,
        "achievements": ["level_5", "boss_slayer"],
        "region": "north",
    },
]

print("=== Game Analytics Dashboard ===\n")

print("=== List Comprehension Examples ===")
high_scorers = [p["name"] for p in players if p["score"] > 2000]
print("High scorers (>2000):", high_scorers)

scores_doubled = [p["score"] * 2 for p in players]
print("Scores doubled:", scores_doubled)

active_players = [p["name"] for p in players if len(p["achievements"]) > 2]
print("Active players:", active_players, "\n")

print("=== Dict Comprehension Examples ===")
player_scores = {player["name"]: player["score"] for player in players}
print("Player scores:", player_scores)

score_categories = {
    "high": sum(1 for p in players if p["score"] > 2000),
    "medium": sum(1 for p in players if 1500 <= p["score"] <= 2000),
    "low": sum(1 for p in players if p["score"] < 1500)
}
print("Score categories:", score_categories)

achievement_counts = {p["name"]: len(p["achievements"]) for p in players}
print("Achievement counts:", achievement_counts, "\n")

print("=== Set Comprehension Examples ===")
unique_players = {p["name"] for p in players}
print("Unique players:", unique_players)

unique_achievements = {ach for p in players for ach in p["achievements"]}
print("Unique achievements:", unique_achievements)

active_regions = {p["region"] for p in players}
print("Active regions:", active_regions, "\n")

print("=== Combined Analysis ===")
total_players = len(players)
total_unique_achievements = len(unique_achievements)
average_score = sum(p["score"] for p in players) / total_players
top_performer = max(players, key=lambda p: p["score"]) if players else None

print(f"Total players: {total_players}")
print(f"Total unique achievements: {total_unique_achievements}")
print(f"Average score: {average_score}")
if top_performer:
    print(
        f"Top performer: {top_performer['name']}"
        f"({top_performer['score']} points, "
        f"{len(top_performer['achievements'])} achievements)"
    )
