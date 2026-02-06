class Plant:
    """Represents a plant with a name."""
    def __init__(self, name: str) -> None:
        self.name = name


def water_plants(plant_list: list[Plant]) -> None:
    """Water each plant in the list, handling
       invalid entries and always cleaning up."""
    s = False
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant.name}")
        s = True
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")
    if s:
        print("Watering completed successfully!")


def test_watering_system() -> None:
    """Test the watering system with normal
       and error-containing plant lists."""
    p_list = [Plant("tomato"), Plant("fern")]
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    water_plants(p_list)
    print("\nTesting with error...")
    corrupted_p_list = [Plant("Lettuce"), None]
    water_plants(corrupted_p_list)
    print("\nCleanup always happens, even with errors!")
test_watering_system()