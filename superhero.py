class Superhero:
    def __init__(self, name, secret_identity, powers, weakness):
        self.name = name
        self._secret_identity = secret_identity  # Encapsulated (private)
        self.powers = powers
        self.weakness = weakness
        self.energy_level = 100
    
    def use_power(self):
        if self.energy_level > 20:
            print(f"{self.name} uses {self.powers[0]}!")
            self.energy_level -= 20
        else:
            print(f"{self.name} is too tired!")
    
    def reveal_secret(self):
        return f"My real name is {self._secret_identity}"

# Test the class
hero = Superhero("Captain Thunder", "John Smith", ["lightning bolts", "flight"], "rubber")
print(hero.name)
hero.use_power()
print(hero.reveal_secret())

class Sidekick(Superhero):
    def __init__(self, name, secret_identity, powers, weakness, mentor):
        super().__init__(name, secret_identity, powers, weakness)
        self.mentor = mentor
    
    def call_for_help(self):
        print(f"{self.name} calls {self.mentor} for backup!")

# Test inheritance
sidekick = Sidekick("Thunder Boy", "Timmy Jones", ["small sparks"], "water", "Captain Thunder")
sidekick.call_for_help()
sidekick.use_power()  # Inherited method