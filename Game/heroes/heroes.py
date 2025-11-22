from abc import ABC, abstractmethod
from attack.damage import Damage

class Hero(ABC):
    def __init__(self, name: str, hp: int, level: int, damage: Damage):
        self.name = name
        self._hp = hp
        self.level = level
        self.damage = damage

    def hp(self):
        return self._hp

    def hp(self, value):
        if value < 0:
            self._hp = 0
        else:
            self._hp = value

    def damage(self, target):
        pass

    def __str__(self):
        return f"Hero: {self.name}"