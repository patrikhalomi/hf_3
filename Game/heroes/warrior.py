from heroes.hero import Hero

class Warrior(Hero):
    def attack(self, target):
        damage = self.damage.calculate()
        target.hp -= damage
        print(f"{self.name} karddal támad és {damage} sebzést okoz {target.name}-nak!")