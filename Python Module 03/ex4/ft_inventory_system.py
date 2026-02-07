import sys
print("=== Inventory System Analysis ===")

def parse_inventory_args(args):
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


inventory = parse_inventory_args(sys.argv[1:])
total_items = 0
for qty in inventory.values():
    total_items += qty
print(f"Total items in inventory: {total_items}")
print(f"Unique item types: {len(inventory)}")
print("=== Current Inventory ===")
for name, qty in inventory.items():
    percent = (qty / total_items) * 100

    unit_word = "unit" if qty == 1 else "units"

    print(f"{name}: {qty} {unit_word} ({percent:.1f}%)")
print("=== Inventory Statistics ===")