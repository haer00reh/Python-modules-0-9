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
tmp_qty = -1
tmpn_qty = None
for name, qty in inventory.items():
    if tmp_qty < qty:
        tmp_qty = qty
        tmpn_qty = name
print(f"Most abundant: {tmpn_qty} ({tmp_qty})")
tmp_qty = None
tmpn_qty = None
for name, qty in inventory.items():
    if tmp_qty is None or tmp_qty > qty:
        tmpn_qty = name
        tmp_qty = qty
print(f"Least abundant: {tmpn_qty} ({tmp_qty})")

item_categories = {"Moderate": {}, "Scarce": {}}

for item, qty in inventory.items():
    if qty >= 5:
        item_categories["Moderate"][item] = qty
    else:
        item_categories["Scarce"][item] = qty

print("=== Item Categories ===")
print(f"Moderate: {item_categories["Moderate"]}")
print(f"Scarce: {item_categories["Scarce"]}")

print("=== Management Suggestions ===")
lst = []
for name, qty in inventory.items():
    if tmp_qty == qty:
        lst.append(name)
print(f"Restock needed: {lst}")
print("=== Dictionary Properties Demo ===")
keys = []
for key in inventory.keys():
    keys.append(key)
print(f"Dictionary keys: {keys}")
vals = []
for value in inventory.values():
    vals.append(value)
print(f"Dictionary values: {vals}")