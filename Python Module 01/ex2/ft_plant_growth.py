class Plant:
    """ a class to represent a plant with name, height and age with
        built in methods to simulate growth of the plant """
    def __init__(self, name, age, height):
        '''the special method to initialize the plant's attributes'''
        self.name = name
        self.age = age
        self.height = height

    def get_info(self):
        '''a method to print the plant's info'''
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def age_older(self, days=1):
        '''a method to increase the plant's age'''
        self.age += days

    def grow(self, days=1):
        '''a method to increase the plant height'''
        self.height += days

    def simulate(self, days):
        ''' a method that simulates the growth of a plant'''
        print(f"=== Day {days} ===")
        self.age_older(days - 1)
        self.grow(days - 1)


days = 7
p1 = Plant("cocoa", 30, 25)
print("=== Day 1 ===")
p1.get_info()
p1.simulate(days)
p1.get_info()
print(f"Growth this week: +{days - 1}cm")
