import random

class Damage:
    def __init__(self, min_damage: int, max_damage: int, level: int):
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.level = level

    def calculate(self, player):
        damage = random.randint(self.min_damage, self.max_damage)
        player.damage = damage
        return damage

    def __add__(self, other): #két sebzés összeadása
        return Damage(self.min_damage, self.max_damage, self.level + other.level)

    def __str__(self):
        return f"Damage: {self.min_damage} {self.max_damage} {self.level}"

    
