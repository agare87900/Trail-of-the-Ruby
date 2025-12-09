class Player:
    def __init__(self, name, health, attack_power, money):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.money = money  # Initialize money

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name} for {self.attack_power} damage!")
        enemy.take_damage(self.attack_power)

    def heal(self):
        heal_amount = 20  # Change heal amount to 20
        self.health += heal_amount
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Current health: {self.health}")

    def is_alive(self):
        return self.health > 0
