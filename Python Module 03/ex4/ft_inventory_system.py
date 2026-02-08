import sys


def parse_inventory_args(args: list[str]) -> dict[str, int]:
    inventory = {}

    for arg in args:
        try:
            name, qty = arg.split(":")
            qty = int(qty)

            if qty < 0:
                raise ValueError("Quantity cannot be negative")

            inventory[name] = inventory.get(name, 0) + qty

        except ValueError:
            print(f"Invalid argument format: '{arg}'. Expected item:quantity")

    return inventory


print("=== Inventory System Analysis ===")

inventory = parse_inventory_args(sys.argv[1:])
total_items = sum(inventory.values())

print(f"Total items in inventory: {total_items}")
print(f"Unique item types: {len(inventory)}")
print("\n=== Current Inventory ===")
for name, qty in inventory.items():
    percent = (qty / total_items) * 100 if total_items else 0.0

    unit_word = "unit" if qty == 1 else "units"

    print(f"{name}: {qty} {unit_word} ({percent:.1f}%)")

print("\n=== Inventory Statistics ===")
if inventory:
    most_abundant = max(inventory, key=inventory.get)
    most_qty = inventory[most_abundant]
    least_abundant = min(inventory, key=inventory.get)
    least_qty = inventory[least_abundant]
    print(f"Most abundant: {most_abundant} ({most_qty})")
    print(f"Least abundant: {least_abundant} ({least_qty})")
else:
    most_abundant = None
    least_abundant = None
    most_qty = None
    least_qty = None
    print("No inventory items available.")

item_categories = {"Moderate": {}, "Scarce": {}}

for item, qty in inventory.items():
    if qty >= 5:
        item_categories["Moderate"][item] = qty
    else:
        item_categories["Scarce"][item] = qty

print("\n=== Item Categories ===")
print(f"Moderate: {item_categories['Moderate']}")
print(f"Scarce: {item_categories['Scarce']}")

print("\n=== Management Suggestions ===")
print(f"Restock needed: {item_categories['Scarce']}")

print("\n=== Dictionary Properties Demo ===")
keys = list(inventory.keys())
print(f"Dictionary keys: {keys}")
vals = list(inventory.values())
print(f"Dictionary values: {vals}")
sample = "helmet"
print(f"Sample lookup - '{sample}' in inventory: {sample in inventory}")
