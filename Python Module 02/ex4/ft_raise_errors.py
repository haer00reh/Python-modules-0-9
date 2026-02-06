class Plant:
    """Represents a plant with a name,
       water level, and sunlight hours."""
    def __init__(self, name: str, water_level: int,
                 sunlight_hours: int) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """Check if a plant's water and sunlight
       levels are within healthy ranges."""
    if plant_name is None:
        raise ValueError("Plant name cannot be empty!")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         "is too high (max 12)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    else:
        return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Test plant health checks with
       various valid and invalid values."""
    print("=== Garden Plant Health Checker ===")
    p_list = [
        Plant("tomato", 8, 5),
        Plant(None, 2, 4),
        Plant("fern", 13, 6),
        Plant("potato", 8, 24),
    ]
    t_list = [
        "\nTesting good values...",
        "\nTesting empty plant name...",
        "\nTesting bad water level...",
        "\nTesting bad sunlight hours...",
    ]
    i = 0
    while i < len(t_list) and i < len(p_list):
        try:
            print(t_list[i])
            result = check_plant_health(
                p_list[i].name, p_list[i].water_level, p_list[i].sunlight_hours
            )
            print(result)
        except ValueError as error:
            print(f"Error: {error}")
        i += 1
test_plant_checks()