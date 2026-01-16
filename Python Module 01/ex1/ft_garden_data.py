class Plant:
    '''a class that represents a plant'''
    def __init__(self, name, age, height):
        '''a special method to initialize the plant's attributes'''
        self.name = name
        self.age = age
        self.height = height

    def infos(self):
        '''a method inside the class to print the plants's infos'''
        print(f"{self.name}: {self.height}cm, {self.age} days old")


print("=== Garden Plant Registry ===")
plants = [
    Plant("Coconut", 340, 200),
    Plant("Carrot", 42, 14),
    Plant("Pea", 32, 7),
    Plant("Pineapple", 54, 34)
]
for each in plants:
    each.infos()
