class plant:
    '''a class that represents a plant'''
    def __init__(self, name, age, height):
        self.age = age
        self.name = name
        self.height = height


class vegetables(plant):
    '''a class that represents a vegetable'''
    def __init__(self, name, age, height, harvest_season, nutrition_value):
        super().__init__(name, age, height)
        self.harvest_season = harvest_season
        self.nutrition_value = nutrition_value

    def get_infos(self):
        '''prints vegetable infos'''
        print(f"{self.name} (Vegetable): {self.height}cm, "
              + "{self.age} days, {self.harvest_season} harvest")

    def value(self):
        '''prints the vegetable nutrition value'''
        print(f"{self.name} is rich with vitamin {self.nutrition_value}")


class tree(plant):
    '''a class that represents a tree'''
    def __init__(self, name, age, height, trunk_diameter, shade):
        super().__init__(name, age, height)
        self.trunk_diameter = trunk_diameter
        self.shade = shade

    def produce_shade(self):
        '''prints the shade produced by the tree'''
        print(f"{self.name} provides {self.shade} square meters of shade")

    def get_infos(self):
        '''prints tree infos'''
        print(f"{self.name} (Tree): {self.height}cm, "
              + "{self.age} days, {self.trunk_diameter}cm diameter")


class flower(plant):
    '''a class that represents a flower'''
    def __init__(self, name, age, height, color):
        super().__init__(name, age, height)
        self.color = color

    def get_infos(self):
        '''prints flower infos'''
        print(f"{self.name} (flower): {self.height}cm, "
              + "{self.age} days, {self.color} color")

    def bloom(self):
        '''indicates that the flower is blooming'''
        print(f"{self.name} is blooming beautifully!")


print("=== Garden Plant Types ===")
print("\n=== trees section ===")
trees = [
    tree("Birch", 521, 1101, 202, 18),
    tree("Acacia", 748, 1202, 212, 26)
]
for each in trees:
    each.get_infos()
    each.produce_shade()
print("\n=== Flowers section ===")
flowers = [
    flower("dandelion", 32, 10, "yellow"),
    flower("poppy", 29, 13, "red")
]
for each in flowers:
    each.get_infos()
    each.bloom()
print("\n=== Vegetables section ===")
veg = [
    vegetables("carrot", 54, 16, "fall", 'C'),
    vegetables("pumpkin", 98, 38, "summer", 'C')
]
for each in veg:
    each.get_infos()
    each.value()
