from alchemy.grimoire import *

print(f"""=== Circular Curse Breaking ===
Testing ingredient validation:
{record_spell("fireball", "fire", validate_ingredients)}
validate_ingredients("fire air"): {validate_ingredients("fire air")}
validate_ingredients("dragon scales"): {validate_ingredients("dragon scales")}

Testing spell recording with validation:
record_spell("Dark Magic", "shadow"): {record_spell("Dark magic", "shadow", validate_ingredients)}

Testing late import technique:
record_spell("Lightning", "air"): {record_spell("Lightning", "air", validate_ingredients)}
Circular dependency curse avoided using late imports!
All spells processed safely!
""")