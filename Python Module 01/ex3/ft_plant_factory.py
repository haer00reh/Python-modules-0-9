class Plant:
    '''a class that represents a plant'''
    total = 0

    def __init__(self, name, age, height):
        '''a special method to initialize the plant's attributes'''
        Plant.total += 1
        self.name = name
        self.age = age
        self.height = height
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


print("=== Plant Factory Output ===")

Plant("Coconut", 340, 200)
Plant("Cactus", 42, 14)
Plant("Potato", 32, 7)
Plant("Pineapple", 54, 34)
Plant("Fern", 23, 33)
Plant("Corn", 21, 65)

print(f"\nTotal plants created {Plant.total}")
