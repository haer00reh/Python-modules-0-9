print("=== Achievement Tracker System ===")
alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
           'speed_demon', 'perfectionist'}
print(f"""
Player alice achievements: {alice}
Player bob achievements: {bob}
Player charlie achievements: {charlie}

=== Achievement Analytics ===

All unique achievements: {alice.union(bob, charlie)}
Total unique achievements: {len(alice.union(bob, charlie))}

Common to all players: {alice.intersection(bob, charlie)}
Rare achievements (1 player): {'collector', 'perfectionist'}

Alice vs Bob common: {alice.intersection(bob)}
Alice unique: {alice.difference(bob)}
Bob unique: {bob.difference(alice)}
""")
