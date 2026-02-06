print("=== Inventory System Analysis ===")
import sys

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
print(inventory)
