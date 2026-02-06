class Plant:
    """Represents a plant with a
       name and wilting status."""
    def __init__(self, name: str, wilting: bool) -> None:
        self.name = name
        self.wilting = wilting

    def check_plant(self) -> None:
        """Raise PlantError if the plant is wilting."""
        if self.wilting is True:
            raise PlantError(f"The {self.name} plant is wilting!")

    @staticmethod
    def check_water(tank: int) -> None:
        """Raise WaterError if the water tank has less than 30 units."""
        if tank < 30:
            raise WaterError("Not enough water in the tank!")


class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when a plant is wilting."""
    pass


class WaterError(GardenError):
    """Raised when there is insufficient water."""
    pass


def catch_all_errors(plant: Plant, tank: int) -> None:
    """Catch and report any PlantError or
       WaterError without stopping the program."""
    print("Testing catching all garden errors...")
    try:
        plant.check_plant()
    except GardenError as error:
        print(f"Caught a garden error: {error}")
    try:
        plant.check_water(tank)
    except GardenError as error:
        print(f"Caught a garden error: {error}")


def errors_ops(plant: Plant, tank: int) -> None:
    """Test PlantError and WaterError separately."""
    print("\nTesting PlantError...")
    try:
        plant.check_plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print("\nTesting WaterError...")
    try:
        plant.check_water(tank)
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")


def test_custom_errors() -> None:
    """Demonstrate custom garden error handling
       with a sample plant and water level."""
    print("=== Custom Garden Errors Demo ===")
    p = Plant("tomato", True)
    water_in_tank = 21
    errors_ops(p, water_in_tank)
    catch_all_errors(p, water_in_tank)
    print("\nAll custom error types work correctly!")
test_custom_errors()