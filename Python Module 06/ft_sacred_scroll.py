import alchemy
import alchemy.elements

print("=== Sacred Scroll Mastery ===\n")
print(f"""Testing direct module access:
alchemy.elements.create_fire(): {alchemy.elements.create_fire()}
alchemy.elements.create_water(): {alchemy.elements.create_water()}
alchemy.elements.create_earth(): {alchemy.elements.create_earth()}
alchemy.elements.create_air(): {alchemy.elements.create_air()}""")
print("\nTesting package-level access (controlled by __init__.py):")
print(f"alchemy.create_fire(): {alchemy.create_fire()}")
print(f"alchemy.create_water(): {alchemy.create_water()}")
try:
    print(f"alchemy.create_earth(): {alchemy.create_earth()}")
except AttributeError:
    print("alchemy.create_earth(): AttributeError - not exposed")
try:
    print(f"alchemy.create_air(): {alchemy.create_air()}")
except AttributeError:
    print("alchemy.create_earth(): AttributeError - not exposed")
print(f"""\nPackage metadata:
Version: {alchemy.__version__}
Author: {alchemy.__author__}""")