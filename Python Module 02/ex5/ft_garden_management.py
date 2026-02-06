class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when there is a
       problem with adding or managing a plant."""
    pass


class WaterError(GardenError):
    """Raised when a plant has an invalid water level."""
    pass


class SunlightError(GardenError):
    """Raised when a plant has an invalid sunlight level."""
    pass


class GardenManager:
    """Manages garden operations like
       adding plants, watering, and health checks."""
    water_in_tank: int = 22

    def __init__(self, name: str, water_level:
                 int, sunlight_hours: int) -> None:
        self.name: str = name
        self.water_level: int = water_level
        self.sunlight: int = sunlight_hours

    @classmethod
    def add_plant(cls, plant_name: str, water_level: int,
                  sunlight_hours: int) -> "GardenManager":
        """Add a plant to the garden and
           return a GardenManager instance."""
        if plant_name is None:
            raise PlantError("error adding plant: "
                             "plant name cannot be empty!!")
        else:
            print(f"added {plant_name} succesfully!")
            return cls(plant_name, water_level, sunlight_hours)

    @staticmethod
    def water_plants(plants: list, water_added: int) -> None:
        """Water all plants in the list,
           cleaning up after each plant."""
        print("Opening watering system")
        try:
            for plant in plants:
                plant.water_level += water_added
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    @classmethod
    def check_water(cls) -> None:
        """Check if there is enough water in the tank."""
        if cls.water_in_tank < 30:
            raise GardenError("Not enough water in the tank!")

    @staticmethod
    def check_plant_health(plants: list) -> None:
        """Check water and sunlight levels
           for all plants and report errors."""
        for plant in plants:
            try:
                if plant.water_level > 10:
                    raise WaterError(f"Water level {plant.water_level} "
                                     "is too high (max 10)")
                elif plant.water_level < 1:
                    raise WaterError(f"Water level {plant.water_level} "
                                     "is too low (min 1)")
                elif plant.sunlight > 12:
                    raise SunlightError(f"Sunlight hours {plant.sunlight} "
                                        "too high max (12)")
                elif plant.sunlight < 2:
                    raise SunlightError(f"Sunlight hours {plant.sunlight} "
                                        " is too low (min 2)")
                else:
                    print(f"{plant.name} is healthy!: Water " 
                          f"{plant.water_level}, sun {plant.sunlight}")
            except (WaterError, SunlightError) as error:
                print(f"Error checking {plant.name}: {error}")


def test_garden_management() -> None:
    """Demonstrate adding plants, watering,
       health checks, and error handling."""
    print("=== Garden Management System ===")
    print("\nAdding plants to garden...")
    try:
        plants = [
            GardenManager.add_plant("tomato", 4, 11),
            GardenManager.add_plant("eggplant", 12, 11),
        ]
        GardenManager.add_plant(None, 7, 12)
    except PlantError as error:
        print(error)

    print("\nWatering plants...")
    GardenManager.water_plants(plants, 3)

    print("\nChecking plant health...")
    GardenManager.check_plant_health(plants)

    print("\nTesting error recovery...")
    try:
        GardenManager.check_water()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")
test_garden_management()