from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life
import alchemy

print(f"""=== Pathway Debate Mastery ===
Testing Absolute Imports (from basic.py):
lead_to_gold(): {lead_to_gold()}
stone_to_gem(): {stone_to_gem()}

Testing Relative Imports (from advanced.py):
philosophers_stone(): {philosophers_stone()}
elixir_of_life(): {elixir_of_life()}

Testing Package Access:
alchemy.transmutation.lead_to_gold(): {alchemy.transmutation.lead_to_gold()}
alchemy.transmutation.advanced.philosophers_stone(): {alchemy.transmutation.advanced.philosophers_stone()}
""")
