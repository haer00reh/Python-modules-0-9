class Plant:
    """Basic plant with a name, height (cm),
    and age (years), supporting growth."""
    kind = "Plant"

    def __init__(self, name, height, age):
        """Initialize a plant with identifying data and starting height/age."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """Increase height by 1cm and report the growth."""
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    """A plant that also has a flower color attribute."""
    kind = "FloweringPlant"

    def __init__(self, name, height, age, color):
        """Initialize a flowering plant with color information."""
        super().__init__(name, height, age)
        self.color = color


class PrizeFlower(FloweringPlant):
    """A flowering plant that carries prize points for scoring."""
    kind = "PrizeFlower"

    def __init__(self, name, height, age, color, points):
        """Initialize a prize flower with its point value."""
        super().__init__(name, height, age, color)
        self.points = points


class Garden:
    """A collection of plants owned by a person,
      tracking growth and scoring."""

    def __init__(self, owner):
        """Create an empty garden for the given owner."""
        self.owner = owner
        self.plants = []
        self.total_growth = 0

    def add_plant(self, plant):
        """Add a plant to the garden and announce it."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        """Grow every plant by 1cm and accumulate total growth."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def calculate_score(self):
        """Compute a score based on height,
          growth, prizes, and flowering count."""
        height = GardenManager.GardenStats.total_height(self.plants)
        prize = GardenManager.GardenStats.total_prize_points(self.plants)
        flowering = GardenManager.GardenStats.count_flowering(self.plants)
        return height + self.total_growth + prize + flowering


class GardenManager:
    """Manage multiple gardens, provide stats, and build score networks."""
    gardens = []
    count = 0

    class GardenStats:
        """Static helpers for aggregating statistics across plants."""
        @staticmethod
        def total_height(plants):
            """Sum heights of all plants in the provided list."""
            total = 0
            for plant in plants:
                total += plant.height
            return total

        @staticmethod
        def total_prize_points(plants):
            """Sum prize points for plants marked as PrizeFlower."""
            total = 0
            for plant in plants:
                if plant.kind == "PrizeFlower":
                    total += plant.points
            return total

        @staticmethod
        def count_flowering(plants):
            """Count plants that are FloweringPlant
              instances by kind marker."""
            count = 0
            for plant in plants:
                if plant.kind == "FloweringPlant":
                    count += 1
            return count

        @staticmethod
        def validate_heights(plants):
            """Validate all plants have positive height; return bool."""
            for plant in plants:
                if plant.height <= 0:
                    return False
            return True

    @classmethod
    def add_garden(cls, owner):
        """Create a new garden, register it, and return it."""
        garden = Garden(owner)
        cls.gardens.append(garden)
        cls.count += 1
        return garden

    @classmethod
    def create_garden_network(cls):
        """Build a mapping of owner names to their calculated garden scores."""
        network = {}
        for i in range(cls.count):
            garden = cls.gardens[i]
            network[garden.owner] = garden.calculate_score()
        return network


print("=== Garden Management System Demo ===")
alice = GardenManager.add_garden("Alice")

alice.add_plant(Plant("Oak Tree", 100, 5))
alice.add_plant(FloweringPlant("Rose", 25, 2, "red"))
alice.add_plant(PrizeFlower("Sunflower", 50, 3, "yellow", 10))

alice.grow_all()

print("=== Alice's Garden Report ===")
print("Plants in garden:")
for plant in alice.plants:
    p = plant
    if p.kind == "PrizeFlower":
        print(f"- {p.name}: {p.height}cm, {p.color}" +
              f" flowers (blooming), Prize points: {p.points}")
    elif p.kind == "FloweringPlant":
        print(f"- {p.name}: {p.height}cm, {p.color} flowers (blooming)")
    else:
        print(f"- {p.name}: {p.height}cm")
plants_count = 0
for plant in alice.plants:
    plants_count += 1
print(f"Plants added: {(plants_count)},"
      + f"Total growth: {alice.total_growth}cm")

regular = 0
flowering = 0
prize = 0

for plant in alice.plants:
    if plant.kind == "PrizeFlower":
        prize += 1
    elif plant.kind == "FloweringPlant":
        flowering += 1
    else:
        regular += 1

print(f"Plant types: {regular} regular,"
      + f" {flowering} flowering, {prize} prize flowers")

print("Height validation test: "
      + f"{GardenManager.GardenStats.validate_heights(alice.plants)}")

scores = GardenManager.create_garden_network()
print(f"Garden scores - Alice: {scores['Alice']}")

print(f"Total gardens managed: {GardenManager.count}")
