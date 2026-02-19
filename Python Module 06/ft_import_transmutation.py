import alchemy.elements
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_earth, create_fire
from alchemy.potions import strength_potion, invisibility_potion

print(f"""\n=== Import Transmutation Mastery ===

Method 1 - Full module import:
alchemy.elements.create_fire(): {alchemy.elements.create_fire()}

Method 2 - Specific function import:
create_water(): {create_water()}

Method 3 - Aliased import:
heal(): {heal()}

Method 4 - Multiple imports:
create_earth(): {create_earth()}
create_fire(): {create_fire()}
strength_potion(): {strength_potion()}
invisibily potion(): {invisibility_potion()}

All import transmutation methods mastered!""")
