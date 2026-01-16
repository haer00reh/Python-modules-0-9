class SecurePlant:
    '''a class that represents a plant'''
    def __init__(self, name, age, height):
        '''a special method to initialize the plant's attributes'''
        print("=== Garden Security System ===")
        self.name = name
        print(f"Plant created: {name}")
        self.age = 0
        self.height = 0
        self.set_age(age)
        self.set_height(height)

    def set_height(self, height):
        '''a method to set the height for a plant securely'''
        if height < 0:
            print("\nInvalid operation attempted: "
                  + f"height {height}cm [REJECTED]\n")
            print("Security: Negative height rejected\n")
            return
        self.height = height
        print(f"height updated successfully {height}cm :)")

    def set_age(self, age):
        '''a method to set the age for a plant securely'''
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} [REJECTED]\n"
                  + "Security: Negative age rejected\n")
            return
        self.age = age
        print(f"age updated successfully {age} :)")

    def get_age(self):
        '''returns plant age'''
        return f"{self.age} days old"

    def get_height(self):
        '''returns plant height'''
        return f"{self.height}cm"


p1 = SecurePlant("Oak", 32, 490)
p1.set_age(-21)
p1.set_height(-212)
print(p1.get_age())
print(p1.get_height())
