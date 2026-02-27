from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine

print("\n=== DataDeck Game Engine ===\n")

factory = FantasyCardFactory()
strategy = AggressiveStrategy()

engine = GameEngine()
engine.configure_engine(factory, strategy)

print("Configuring Fantasy Card Game...")
print(f"Factory: {factory.__class__.__name__}")
print(f"Strategy: {strategy.get_strategy_name()}")
print(f"Available types: {factory.get_supported_types()}")

print("\nSimulating aggressive turn...")
engine.simulate_turn()

print("\nGame Report:")
print(engine.get_engine_status())

print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
