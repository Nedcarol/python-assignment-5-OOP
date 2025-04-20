class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Fish(Animal):
    def move(self):
        return f"{self.name} is swimming! 🐟"

class Bird(Animal):
    def move(self):
        return f"{self.name} is flying! 🦅"

class Snake(Animal):
    def move(self):  # Added 'def' that was missing
        return f"{self.name} is slithering! 🐍"

class Dog(Animal):
    def move(self):
        return f"{self.name} is running! 🐕"

# Test polymorphism
animals = [Fish("Nemo"), Bird("Eagle")]
for animal in animals:
    print(animal.move())

# Update the test loop
animals.extend([Snake("Viper"), Dog("Buddy")])  # Fixed Snake spelling
for animal in animals:
    print(animal.move())git