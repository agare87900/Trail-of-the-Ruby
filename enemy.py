class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, player):
        print(f"{self.name} attacks {player.name} for {self.attack_power} damage!")
        player.take_damage(self.attack_power)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Current health: {self.health}")

    def is_alive(self):
        return self.health > 0
