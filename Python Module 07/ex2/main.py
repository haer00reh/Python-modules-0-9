from ex2.EliteCard import EliteCard

try:
    print("=== DataDeck Ability System ===")

    elite = EliteCard(
        'Arcane Warrior', 12, 'Mythical',
        'Melee & Spellcasting', 9, 5, 8)

    print(f"""\nEliteCard capabilities:
- Card: ['play', 'get_card_info', 'is_playable']
- Combatable: ['attack', 'defend', 'get_combat_stats']
- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']

Playing Arcane Warrior (Elite Card):

Combat phase:
Attack result: {elite.attack('Enemy')}
Defense result: {elite.defend(2)}

Magic phase:
Spell cast: {elite.cast_spell('Fireball', ['Baby dragon', 'Copy cat'])}
Mana channel: {elite.channel_mana(3)}

Multiple interface implementation successful!
""")
except Exception as e:
    print(f"Error in main execution: {e}")
