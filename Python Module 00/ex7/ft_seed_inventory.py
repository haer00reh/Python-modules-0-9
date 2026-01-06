def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit != "packets" and unit != "grams" and unit != "area":
        print("Unknown unit type")
        return
    if unit == "packets":
        print(seed_type.capitalize() + f" seeds: {quantity} packets available")
    elif unit == "area":
        print(seed_type.capitalize() +
              f" seeds: covers {quantity} square meters")
    elif unit == "grams":
        print(seed_type.capitalize() + f" seeds: {quantity} grams total")
